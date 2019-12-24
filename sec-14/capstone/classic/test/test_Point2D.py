# asarkar:sec-14$ python -m unittest discover

import unittest
from capstone.classic.point_2d import Point2D

class TestPoint2D(unittest.TestCase):
	def test_init(self):
		p = Point2D(1, 2)
		self.assertEqual(p.x, 1)
		self.assertEqual(p.y, 2)

	def test_eq(self):
		p1 = Point2D(1, 2)
		p2 = Point2D(1, 2)

		self.assertTrue(p1 == p2)

	def test_ne(self):
		p1 = Point2D(1, 2)
		p2 = Point2D(1, 3)

		self.assertFalse(p1 == p2)

	def test_lt(self):
		p1 = Point2D(1, 2)
		p2 = Point2D(2, 2)

		self.assertTrue(p1 < p2)

	def test_le(self):
		p1 = Point2D(1, 2)
		p2 = Point2D(1, 2)

		self.assertTrue(p1 <= p2)

	def test_gt(self):
		p1 = Point2D(2, 2)
		p2 = Point2D(1, 2)

		self.assertTrue(p1 > p2)

	def test_ge(self):
		p1 = Point2D(1, 2)
		p2 = Point2D(1, 2)

		self.assertTrue(p1 >= p2)

	def test_dist(self):
		p1 = Point2D(1, 2)
		p2 = Point2D(1, 3)

		self.assertEqual(p1.dist(p2), 1)

	def test_str(self):
		p = Point2D(1, 2)

		self.assertEqual(str(p), "(1, 2)")
