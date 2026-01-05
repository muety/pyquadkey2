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

	def testFromString(self):
		pass

	def testToString(self):
		pass

	def testGetQuadKey(self):
		pass

	def testGetCoordinates(self):
		pass
