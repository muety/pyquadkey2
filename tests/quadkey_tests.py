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

	def testGetQuadKey(self):
		geo = (40, -105)
		level = 7 
		key = QuadKey('0231010')
		self.assertEqual(key, QuadKey.from_geo(geo, level))

	def testEquality(self):
		one = QuadKey('00')
		two = QuadKey('00')
		self.assertEqual(one, two)
		three = QuadKey('0')
		self.assertNotEqual(one, three)
		

	def testChildren(self):
		qk = QuadKey('0') 
		self.assertEqual([c.key for c in qk.children()], ['00','01', '02', '03'])
		qk = QuadKey(''.join(['0' for x in xrange(23)]))
		self.assertEqual(qk.children(), [])

	def testAncestry(self):
		one = QuadKey('0')
		two = QuadKey('0101')
		self.assertEqual(3, one.is_descendent(two))
		self.assertIsNone(two.is_descendent(one))
		self.assertEqual(3, two.is_ancestor(one))
		three = QuadKey('1')
		self.assertIsNone(three.is_ancestor(one))

	def testNearby(self):
		qk = QuadKey('0')
		self.assertEqual(set(['1','2','3']), set(qk.nearby()))
		qk = QuadKey('01')
		print qk
		print qk.nearby()
		self.assertEqual(set(['00','10','02','03','13','33','32','23']), set(qk.nearby()))

