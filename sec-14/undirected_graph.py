from __future__ import annotations # for Edge forward references
from functools import total_ordering
from typing import List

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

class UndirectedGraph:
	def __init__(self):
		self.adj = dict()

	def vertices(self) -> List[int]:
		return list(self.adj.keys())

	def add_edge(self, e: Edge) -> None:
		if e.tail not in self.adj:
			self.adj[e.tail] = set()
		if e.head not in self.adj:
			self.adj[e.head] = set()

		self.adj[e.head].add(e)
		self.adj[e.tail].add(e)

	def adj_edges(self, v: int) -> List[Edge]:
		if v not in self.adj:
			return None
		return self.adj[v]

	def degree(self, v: int) -> int:
		if v not in self.adj:
			return None
		return len(self.adj[v])

	def __repr__(self) -> str:
		return f"{self.adj}"