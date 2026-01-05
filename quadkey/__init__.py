import itertools
import re
from enum import IntEnum
from typing import Tuple, List, Iterable, Generator, Dict

try:
    from pyquadkey2 import tilesystem
except ModuleNotFoundError:
    from .tilesystem import tilesystem

from .util import precondition

LAT_STR: str = 'lat'
LON_STR: str = 'lon'
LATITUDE_RANGE: Tuple[float, float] = (-85.05112878, 85.05112878)
LONGITUDE_RANGE: Tuple[float, float] = (-180., 180.)
# Due to the way quadkeys are represented as 64-bit integers (https://github.com/joekarl/binary-quadkey/blob/64f76a15465169df9d0d5e9e653906fb00d8fa48/example/java/src/main/java/com/joekarl/binaryQuadkey/BinaryQuadkey.java#L67),
# we can not use 31 character quadkeys, but only 29, since five bits explicitly encode the zoom level
LEVEL_RANGE: Tuple[int, int] = (1, 29)
KEY_PATTERN: re = re.compile("^[0-3]+$")


class TileAnchor(IntEnum):
    ANCHOR_NW = 0
    ANCHOR_NE = 1
    ANCHOR_SW = 2
    ANCHOR_SE = 3
    ANCHOR_CENTER = 4


def valid_level(level: int) -> bool:
    return LEVEL_RANGE[0] <= level <= LEVEL_RANGE[1]


def valid_geo(lat: float, lon: float) -> bool:
    return LATITUDE_RANGE[0] <= lat <= LATITUDE_RANGE[1] and LONGITUDE_RANGE[0] <= lon <= LONGITUDE_RANGE[1]


def valid_key(key: str) -> bool:
    return KEY_PATTERN.match(key) is not None


class QuadKey:
    @precondition(lambda c, key: valid_key(key))
    def __init__(self, key: str):
        self.key: str = key
        tile_tuple: Tuple[Tuple[int, int], int] = tilesystem.quadkey_to_tile(self.key)
        self.tile: Tuple[int, int] = tile_tuple[0]
        self.level: int = tile_tuple[1]

    def children(self, at_level: int = -1) -> List['QuadKey']:
        if at_level <= 0:
            at_level = self.level + 1

        if self.level >= LEVEL_RANGE[1] or at_level > LEVEL_RANGE[1] or at_level <= self.level:
            return []

        return [QuadKey(self.key + ''.join(k)) for k in itertools.product('0123', repeat=at_level - self.level)]

    def parent(self) -> 'QuadKey':
        return QuadKey(self.key[:-1])

    def nearby_custom(self, config: Tuple[Iterable[int], Iterable[int]]) -> List[str]:
        perms = set(itertools.product(config[0], config[1]))
        tiles = set(map(lambda perm: (abs(self.tile[0] + perm[0]), abs(self.tile[1] + perm[1])), perms))
        return [tilesystem.tile_to_quadkey(tile, self.level) for tile in tiles]

    def nearby(self, n: int = 1) -> List[str]:
        return self.nearby_custom((range(-n, n + 1), range(-n, n + 1)))

    def is_ancestor(self, node: 'QuadKey') -> bool:
        return not (self.level <= node.level or self.key[:len(node.key)] != node.key)

    def is_descendent(self, node) -> bool:
        return node.is_ancestor(self)

    def side(self) -> float:
        return 256 * tilesystem.ground_resolution(0, self.level)

    def area(self) -> float:
        side = self.side()
        return side * side

    @staticmethod
    def xdifference(first: 'QuadKey', second: 'QuadKey') -> Generator['QuadKey', None, None]:
        x, y = 0, 1
        assert first.level == second.level
        self_tile = list(first.to_tile()[0])
        to_tile = list(second.to_tile()[0])
        se, sw, ne, nw = None, None, None, None
        if self_tile[x] >= to_tile[x] and self_tile[y] <= to_tile[y]:
            ne, sw = self_tile, to_tile
        elif self_tile[x] <= to_tile[x] and self_tile[y] >= to_tile[y]:
            sw, ne = self_tile, to_tile
        elif self_tile[x] <= to_tile[x] and self_tile[y] <= to_tile[y]:
            nw, se = self_tile, to_tile
        elif self_tile[x] >= to_tile[x] and self_tile[y] >= to_tile[y]:
            se, nw = self_tile, to_tile
        cur = ne[:] if ne else se[:]
        while cur[x] >= (sw[x] if sw else nw[x]):
            while (sw and cur[y] <= sw[y]) or (nw and cur[y] >= nw[y]):
                yield from_tile(tuple(cur), first.level)
                cur[y] += 1 if sw else -1
            cur[x] -= 1
            cur[y] = ne[y] if ne else se[y]

    def difference(self, to: 'QuadKey') -> List['QuadKey']:
        return [qk for qk in self.xdifference(self, to)]

    @staticmethod
    def bbox(quadkeys: List['QuadKey']) -> List['QuadKey']:
        assert len(quadkeys) > 0

        level = quadkeys[0].level
        tiles = [qk.to_tile()[0] for qk in quadkeys]
        x, y = zip(*tiles)
        ne = from_tile((max(x), min(y)), level)
        sw = from_tile((min(x), max(y)), level)

        return ne.difference(sw)

    def to_tile(self) -> Tuple[Tuple[int, int], int]:
        return self.tile, self.level

    def to_pixel(self, anchor: TileAnchor = TileAnchor.ANCHOR_NW) -> Tuple[int, int]:
        return tilesystem.tile_to_pixel(self.tile, anchor)

    def to_geo(self, anchor: TileAnchor = TileAnchor.ANCHOR_NW) -> Tuple[float, float]:
        pixel = tilesystem.tile_to_pixel(self.tile, anchor)
        return tilesystem.pixel_to_geo(pixel, self.level)

    def to_quadint(self) -> int:
        return tilesystem.quadkey_to_quadint(self.key)

    def set_level(self, level: int):
        assert level < self.level
        self.key = self.key[:level]
        self.tile, self.level = tilesystem.quadkey_to_tile(self.key)

    def __eq__(self, other):
        return isinstance(other, QuadKey) and self.key == other.key

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.key.__lt__(other.key)

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key

    def __hash__(self):
        return hash(self.key)


@precondition(lambda geo, level: valid_geo(*geo) and valid_level(level))
def from_geo(geo: Tuple[float, float], level: int) -> 'QuadKey':
    pixel = tilesystem.geo_to_pixel(geo, level)
    tile = tilesystem.pixel_to_tile(pixel)
    key = tilesystem.tile_to_quadkey(tile, level)
    return QuadKey(key)


def from_tile(tile: Tuple[int, int], level: int) -> 'QuadKey':
    return QuadKey(tilesystem.tile_to_quadkey(tile, level))


def from_str(qk_str: str) -> 'QuadKey':
    return QuadKey(qk_str)


def from_int(qk_int: int) -> 'QuadKey':
    return QuadKey(tilesystem.quadint_to_quadkey(qk_int))


@precondition(lambda geo: valid_geo(*geo))
def geo_to_dict(geo: Tuple[float, float]) -> Dict[str, float]:
    return {LAT_STR: geo[0], LON_STR: geo[1]}
