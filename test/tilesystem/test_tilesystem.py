import unittest
from unittest import TestCase

from quadkey import TileAnchor
from quadkey.tilesystem import tilesystem


class TileSystemTest(TestCase):
    def testGroundResolution(self):
        geo = (40., -105.)
        res = 936.87
        self.assertAlmostEqual(res, tilesystem.ground_resolution(geo[0], 7), 2)

    def testGeoToPixel(self):
        geo = (40., -105.)
        level = 7
        pixel = (6827, 12405)
        self.assertEqual(pixel, tilesystem.geo_to_pixel(geo, level))

    def testPixelToGeo(self):
        pixel = (6827, 12405)
        level = 7
        geo = (40.002372, -104.996338)
        self.assertEqual(geo, tilesystem.pixel_to_geo(pixel, level))

    def testPixelToTile(self):
        pixel = (6827, 12405)
        tile = (26, 48)
        self.assertEqual(tile, tilesystem.pixel_to_tile(pixel))

    def testTileToPixel(self):
        tile = (26, 48)
        pixel = (6656, 12288)
        self.assertEqual(pixel, tilesystem.tile_to_pixel(tile, TileAnchor.ANCHOR_NW))

    def testTileToQuadkey(self):
        tile = (26, 48)
        level = 7
        key = '0231010'
        self.assertEqual(key, tilesystem.tile_to_quadkey(tile, level))

    def testQuadkeyToTile(self):
        tile = (26, 48)
        level = 7
        key = '0231010'
        self.assertEqual((tile, level), tilesystem.quadkey_to_tile(key))


if __name__ == '__main__':
    unittest.main()
