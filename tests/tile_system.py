import unittest
from unittest import TestCase
from quadkey.tile_system import TileSystem

class TileSystemTest(TestCase):

	def testClip(self):
		self.assertEqual(1, TileSystem.clip(0, (1,5)) )
		self.assertEqual(5, TileSystem.clip(10, (1,5)) )
		self.assertEqual(3, TileSystem.clip(3, (1,5)) )
		with self.assertRaises(AssertionError):
			TileSystem.clip(7, (5,1))


	def testMapSize(self):
		self.assertEqual(512, TileSystem.map_size(1))
		with self.assertRaises(AssertionError):
			TileSystem.map_size(0)

	def testGroundResolution(self):
		TileSystem.ground_resolution(45, 7)

	def testMapScale(self):
		TileSystem.map_scale(45, 7, 45)

	def testGeoToPixel(self):
		geo = (-105, 45)
		level = 7
		TileSystem.geo_to_pixel(geo, level)

	def testPixelToGeo(self):
		pixel = (50, 45)
		level = 7
		TileSystem.pixel_to_geo(pixel, level)

	def testPixelToTile(self):
		pixel = (50, 45)
		TileSystem.pixel_to_tile(pixel)

	def testTileToPixel(self):
		tile = (3,3)
		TileSystem.tile_to_pixel(tile)

	def testTileToQuadkey(self):
		tile = (3,3)
		level = 7
		TileSystem.tile_to_quadkey(tile, level)

	def testQuadkeyToTile(self):
		quadkey = '00'
		TileSystem.quadkey_to_tile(quadkey)
