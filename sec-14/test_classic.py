# asarkar:sec-14$ python -m unittest discover

import unittest
import classic

class TestClassic(unittest.TestCase):
	def test_collatz(self):
		self.assertEqual(classic.collatz(12), 10)
		self.assertEqual(classic.collatz(19), 21)

	def test_closest_pair(self):
		p1 = classic.Point2D(2, 3)
		p2 = classic.Point2D(3, 4)
		closest = classic.closest_pair([
			p1,
			classic.Point2D(12, 30),
			classic.Point2D(40, 50),
			classic.Point2D(5, 1),
			classic.Point2D(12, 10),
			p2
		])
		self.assertEqual(closest, (p1, p2))

	def test_sieve_of_eratosthenes(self):
		self.assertEqual(classic.sieve_of_eratosthenes(50), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

	def test_bubble_sort(self):
		l = [10, 3, 5, 12, 9, 10]
		classic.bubble_sort(l)
		self.assertEqual(l, [3, 5, 9, 10, 10, 12])