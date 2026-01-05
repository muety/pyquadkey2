import unittest
from unittest import TestCase
from quadkey import QuadKey

class QuadKeyTest(TestCase):

	def testInit(self):
		pass

	def testFromString(self):
		pass

	def testToString(self):
		pass

	def testGetQuadKey(self):
		geo = (40, -105)
		level = 7 
		key = '0231010'
		self.assertEqual(key, QuadKey.get_quadkey(geo, level))

	def testGetCoordinates(self):
		pass
