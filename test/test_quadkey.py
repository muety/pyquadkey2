import unittest
from operator import attrgetter
from unittest import TestCase

import quadkey


class QuadKeyTest(TestCase):
    def testInit(self):
        key = '0321201120'
        qk = quadkey.from_str(key)
        self.assertIsInstance(qk, quadkey.QuadKey)
        self.assertEqual(key, qk.key)

    def testInitEmptyInput(self):
        with self.assertRaises(AssertionError):
            quadkey.from_str('')

    def testInitInvalidKey(self):
        with self.assertRaises(AssertionError):
            quadkey.from_str('0156510012')

    def testFromGeo(self):
        self.assertEqual('1202032333311320', quadkey.from_geo((49.014205, 8.420025), 16).key)

    def testFromGeoInvalidLevel(self):
        with self.assertRaises(AssertionError):
            quadkey.from_geo((49.014205, 8.420025), 32)

    def testEquality(self):
        one = quadkey.from_str('00')
        two = quadkey.from_str('00')
        three = quadkey.from_str('0')
        self.assertEqual(one, two)
        self.assertNotEqual(one, three)

    def testSortability(self):
        keys = [quadkey.from_str(s) for s in ['200', '100']]
        keys_ordered = [quadkey.from_str(s) for s in ['100', '200']]
        self.assertEqual(keys_ordered, sorted(keys))

    def testChildren(self):
        qk = quadkey.from_str('0')
        self.assertEqual({'00', '01', '02', '03'}, set([c.key for c in qk.children()]))

    def testChildrenMaxLevel(self):
        qk = quadkey.from_str(''.join(['0'] * quadkey.LEVEL_RANGE[1]))
        self.assertEqual(set(), set(qk.children()))

    def testChildrenAtLevel(self):
        qk = quadkey.from_str('0')
        expected_children = set(map(quadkey.from_str, ['000', '001', '002', '003', '010', '011', '012', '013', '020', '021', '022', '023', '030', '031', '032', '033']))
        self.assertEqual(expected_children, set(qk.children(at_level=3)))

    def testChildrenAtInvalidLevel(self):
        qk = quadkey.from_str('0')
        self.assertEqual(set(), set(qk.children(at_level=32)))

    def testParent(self):
        self.assertEqual(quadkey.from_str('000'), quadkey.from_str('0001').parent())

    def testParentMinLevel(self):
        with self.assertRaises(AssertionError):
            quadkey.from_str('0').parent()

    def testAncestorDescendent(self):
        one = quadkey.from_str('0')
        two = quadkey.from_str('0101')
        three = quadkey.from_str('1')
        self.assertTrue(one.is_descendent(two))
        self.assertFalse(two.is_descendent(one))
        self.assertTrue(two.is_ancestor(one))
        self.assertFalse(three.is_ancestor(one))

    def testNearby(self):
        self.assertEqual({'0', '1', '2', '3'}, set(quadkey.from_str('0').nearby()))
        self.assertEqual({'00', '01', '10', '02', '03', '12'}, set(quadkey.from_str('01').nearby()))

    def testNearbyWithRadius(self):
        self.assertEqual(
            {'023', '012', '103', '212', '021', '303', '033', '300', '203', '030', '211', '102', '003', '301', '031', '302', '201', '032', '120', '123', '213', '013', '122', '121', '210'},
            set(quadkey.from_str('033').nearby(n=2))
        )

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

    def testBbox(self):
        qk1 = quadkey.QuadKey('033')
        qk2 = quadkey.QuadKey('003')
        bbox = quadkey.QuadKey.bbox([qk1, qk2])
        self.assertEqual({'033', '031', '013', '032', '030', '012', '023', '021', '003'}, set(map(attrgetter('key'), bbox)))

    def testSide(self):
        qk = quadkey.QuadKey(''.join(['0'] * 10))
        self.assertEqual(int(qk.side()), 39135)

    def testArea(self):
        qk = quadkey.QuadKey(''.join(['0'] * 10))
        self.assertEqual(int(qk.area()), 1531607591)


if __name__ == '__main__':
    unittest.main()
