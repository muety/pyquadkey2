from util import precondition
from tile_system import TileSystem

class QuadKey:

	def __init__(self, geo, level):
		# assert lat, lon and level are valid
		self.key = QuadKey.get_quadkey(geo, level)
		self.geo = geo
		self.latititude = geo[0]
		self.longitude = geo[1]
		self.level = level

	def __str__(self):
		return self.key

	def __repr__(self):
		return self.key

	@classmethod
	def from_str(cls, key):
		level = len(key)
		geo = QuadKey.get_coordinates(key)
		return cls(geo, level)

	@staticmethod
	def get_quadkey(geo, level):	
		pixel = TileSystem.geo_to_pixel(geo, level)
		tile = TileSystem.pixel_to_tile(pixel)
		quadkey = TileSystem.tile_to_quadkey(tile, level)
		return quadkey

	@staticmethod
	def get_coordinates(key):
		pass

