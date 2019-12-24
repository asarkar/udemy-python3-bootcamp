from .point_2d import Point2D
import math
from heapq import heappush, heappop
from typing import List, Sequence

# https://en.wikipedia.org/wiki/Collatz_conjecture
def collatz(n):
	if n <= 0:
		raise ValueError(f"{n} is not a positive integer")
	# the sequence includes n
	count = 1

	while (n != 1):
		if n % 2 == 0:
			n /= 2
		else:
			n = 3 * n + 1
		count += 1

	return count

# Algorithm Design - Kleinberg + Tardos, sec 5.4
# https://www.youtube.com/watch?v=xi-WF07rAQw
# https://www.youtube.com/watch?v=3pUOv_ocJyA
# https://www.youtube.com/watch?v=7tiafUFrlBw
def closest_pair(points: Sequence[Point2D]) -> (Point2D, Point2D):
	inf = Point2D(math.inf, math.inf) # type(math.inf) is float but there is no integer infinity

	def __closest_pair(p_x: List[Point2D], p_y: List[Point2D]) -> (Point2D, Point2D):
		# print(f"p_x = {p_x}, p_y = {p_y}")
		n = len(p_x)
		assert len(p_y) == n, "Length of the sublists don't match"
		if n <= 3: # find closest pair by measuring all pairwise distances
			l = [(p_x[i], p_x[i + 1]) for i in range(n - 1)]
			return min(l, key = lambda x: x[0].dist(x[1]), default = (p_x[0], inf))

		# split Px and Py, and recurse
		mid_x = p_x[math.floor(n / 2)].x
		q_x, q_y, r_x, r_y = [], [], [], []

		for i in range(n):
			if p_x[i].x <= mid_x:
				q_x.append(p_x[i])
			else:
				r_x.append(p_x[i])
			if p_y[i].x <= mid_x:
				q_y.append(p_y[i])
			else:
				r_y.append(p_y[i])

		# print(f"mid_x = {mid_x}, q_x = {q_x}, q_y = {q_y}, r_x = {r_x}, r_y = {r_y}")
		q = __closest_pair(q_x, q_y)
		r = __closest_pair(r_x, r_y)

		# find closest pair between Q and R
		closest = min(q, r, key = lambda x: x[0].dist(x[1]))
		d = closest[0].dist(closest[1])
		# print(f"closest = {closest}, d = {d}")

		# find closest split pair
		p = q_x[-1]
		s_y = list(filter(lambda a: a.x >= p.x - d, q_y)) + list(filter(lambda b: b.x <= p.x + d, r_y))
		# print(f"p = {p}, s_y = {s_y}")

		n = len(s_y)
		for i in range(n - 1):
			for j in range(i + 1, min(n, i + 8)):
				pair = (s_y[i], s_y[j])
				tmp = pair[0].dist(pair[1])
				# print(f"pair = {pair}, tmp = {tmp}")
				if tmp < d:
					d = tmp
					closest = pair
					# print(f"Updated: closest = {closest}, d = {d}")

		return closest

	return __closest_pair(sorted(points), sorted(points, key = lambda p: p.y))

def sieve_of_eratosthenes(n: int) -> List[int]:
	x = math.sqrt(n)
	primes = []
	composites = []

	for i in range(2, n):
		if not composites or composites[0][0] != i:
			primes.append(i)
			j = i * i
			if (i <= x):
				heappush(composites, (j, i))
		else:
			while composites and composites[0][0] == i:
				(j, k) = heappop(composites)
				if (j + k <= n):
					heappush(composites, (j + k, k))

	return primes

def bubble_sort(l: Sequence[int]) -> None:
	last_unsorted = len(l) - 1
	sorted = False
	while last_unsorted > 0 and not sorted: # short circuit if already sorted
		sorted = True
		for i in range(last_unsorted):
			if (l[i] > l[i + 1]):
				tmp = l[i]
				l[i] = l[i + 1]
				l[i + 1] = tmp

				sorted = False
		# each pass through the array moves the largest yet unsorted element to its rightful place at the end
		last_unsorted -= 1



