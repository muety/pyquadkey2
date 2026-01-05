import unittest
from unittest import TestCase

import quadkey


class QuadKeyTest(TestCase):

    def testInit(self):
        qk = quadkey.from_str('0321201120')
        self.assertIsInstance(qk, quadkey.QuadKey)
        with self.assertRaises(AssertionError):
            quadkey.from_str('')
        with self.assertRaises(AssertionError):
            quadkey.from_str('0156510012')

    def testFromGeo(self):
        geo = (40, -105)
        level = 7
        key = quadkey.from_str('0231010')
        self.assertEqual(key, quadkey.from_geo(geo, level))

    def testEquality(self):
        one = quadkey.from_str('00')
        two = quadkey.from_str('00')
        self.assertEqual(one, two)
        three = quadkey.from_str('0')
        self.assertNotEqual(one, three)

    def testChildren(self):
        qk = quadkey.from_str('0')
        self.assertEqual({'00', '01', '02', '03'}, set([c.key for c in qk.children()]))

        qk = quadkey.from_str(''.join(['0'] * quadkey.LEVEL_RANGE[1]))
        self.assertEqual(set(), set(qk.children()))

        qk = quadkey.from_str('0')
        expected_children = set(map(quadkey.from_str, ['000', '001', '002', '003', '010', '011', '012', '013', '020', '021', '022', '023', '030', '031', '032', '033']))
        self.assertEqual(expected_children, set(qk.children(at_level=3)))

    def testAncestor(self):
        one = quadkey.from_str('0')
        two = quadkey.from_str('0101')
        self.assertTrue(one.is_descendent(two))
        self.assertFalse(two.is_descendent(one))
        self.assertTrue(two.is_ancestor(one))
        three = quadkey.from_str('1')
        self.assertFalse(three.is_ancestor(one))

    def testNearby(self):
        qk = quadkey.from_str('0')
        self.assertEqual({'0', '1', '2', '3'}, set(qk.nearby()))
        qk = quadkey.from_str('01')
        self.assertEqual({'00', '01', '10', '02', '03', '12'}, set(qk.nearby()))

    def testDifference(self):
        _from = quadkey.from_str('0320101102')
        _to = quadkey.from_str('0320101110')
        diff = {'0320101102', '0320101100', '0320101103', '0320101101', '0320101112', '0320101110'}
        self.assertEqual(diff, set([qk.key for qk in _to.difference(_from)]))
        self.assertEqual(diff, set([qk.key for qk in _from.difference(_to)]))

    def testDifference2(self):
        qk1 = quadkey.QuadKey('033')
        qk2 = quadkey.QuadKey('003')
        diff = [qk.key for qk in qk1.difference(qk2)]
        self.assertEqual(set(diff), {'033', '031', '013', '032', '030', '012', '023', '021', '003'})

    def testDifference3(self):
        qk1 = quadkey.QuadKey('021')
        qk2 = quadkey.QuadKey('011')
        diff = [qk.key for qk in qk1.difference(qk2)]
        self.assertEqual(set(diff), {'011', '013', '031', '010', '012', '030', '001', '003', '021'})

    def testSide(self):
        qk = quadkey.QuadKey(''.join(['0'] * 10))
        self.assertEqual(int(qk.side()), 39135)

    def testArea(self):
        qk = quadkey.QuadKey(''.join(['0'] * 10))
        self.assertEqual(int(qk.area()), 1531607591)


if __name__ == '__main__':
    unittest.main()
