import unittest
from unittest import TestCase

from quadkey import TileAnchor
from quadkey.tilesystem import tilesystem


class TileSystemTest(TestCase):
    def testGroundResolution(self):
        self.assertAlmostEqual(936.87, tilesystem.ground_resolution(40., 7), 2)

    def testGeoToPixel(self):
        self.assertEqual((6827, 12405), tilesystem.geo_to_pixel((40., -105.), 7))

    def testGeoToPixelClip(self):
        self.assertEqual(tilesystem.geo_to_pixel((40., 180.), 7), tilesystem.geo_to_pixel((40., 181.), 7))

    def testPixelToGeo(self):
        self.assertEqual((40.002372, -104.996338), tilesystem.pixel_to_geo((6827, 12405), 7))

    def testPixelToTile(self):
        self.assertEqual((26, 48), tilesystem.pixel_to_tile((6827, 12405)))

    def testTileToPixel(self):
        self.assertEqual((6656, 12288), tilesystem.tile_to_pixel((26, 48), TileAnchor.ANCHOR_NW))

    def testTileToQuadkey(self):
        self.assertEqual('0231010', tilesystem.tile_to_quadkey((26, 48), 7))

    def testQuadkeyToTile(self):
        self.assertEqual(((26, 48), 7), tilesystem.quadkey_to_tile('0231010'))

    def testQuadkeyToQuadint(self):
        self.assertEqual(1953184653288407055, tilesystem.quadkey_to_quadint('012301230123012'))
        self.assertEqual(1379860704579813385, tilesystem.quadkey_to_quadint('010302121'))

    def testQuadintToQuadkey(self):
        self.assertEqual('012301230123012', tilesystem.quadint_to_quadkey(1953184653288407055))
        self.assertEqual('010302121', tilesystem.quadint_to_quadkey(1379860704579813385))


if __name__ == '__main__':
    unittest.main()
