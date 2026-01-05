import unittest
from unittest import TestCase
from quadkey import QuadKey

class QuadKeyTest(TestCase):

	def testInit(self):
		qk = QuadKey('0321201120')
		with self.assertRaises(AssertionError):
			qk = QuadKey('')
		with self.assertRaises(AssertionError):
			qk = QuadKey('0156510012')

	def testFromString(self):
		pass

	def testToString(self):
		pass

	def testGetQuadKey(self):
		geo = (40, -105)
		level = 7 
		key = QuadKey('0231010')
		self.assertEqual(key, QuadKey.from_geo(geo, level))

	def testGetCoordinates(self):
		pass

	def testIsParent(self):
		child = QuadKey('0011')
		parent = QuadKey('00')
		self.assertTrue(child.is_parent(parent))
