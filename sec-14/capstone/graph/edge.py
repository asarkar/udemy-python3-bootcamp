from __future__ import annotations # for Edge forward references
from functools import total_ordering

@total_ordering # generate comparison methods
class Edge:
	def __init__(self, tail: int, head: int, weight: float = 0):
		self.tail = tail
		self.head = head
		self.weight = weight

	def other(self, v: int) -> int:
		if v == self.tail:
			return self.head
		return self.tail

	def __vertices(self) -> (int, int):
		if self.tail < self.head:
			return (self.tail, self.head)
		return (self.head, self.tail)

	def __hash__(self):
		return hash(self.__vertices() + (self.weight, ))

	def __repr__(self) -> str:
		return f"{self.__vertices() + (self.weight, )}"

	def __eq__(self, other: Edge) -> bool:
		return self.__vertices() == other.__vertices()

	def __lt__(self, other: Point2D) -> bool:
		return self.__vertices() < other.__vertices()