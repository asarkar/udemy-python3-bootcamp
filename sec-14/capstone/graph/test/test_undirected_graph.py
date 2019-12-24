# asarkar:sec-14$ python -m unittest discover

import unittest
from capstone.graph.undirected_graph import UndirectedGraph
from capstone.graph.edge import Edge

class TestUndirectedGraph(unittest.TestCase):
	def test_init(self):
		g = UndirectedGraph()
		self.assertEqual(len(g.vertices()), 0)

	def test_graph(self):
		g = UndirectedGraph()
		g.add_edge(Edge(0, 1))
		g.add_edge(Edge(0, 2))
		g.add_edge(Edge(0, 3))
		g.add_edge(Edge(1, 2))
		g.add_edge(Edge(1, 3))
		g.add_edge(Edge(3, 4))

		self.assertEqual(sorted(g.vertices()), list(range(5)))

		self.assertEqual(sorted(g.adj_edges(0)), [Edge(0, 1), Edge(0, 2), Edge(0, 3)])
		self.assertEqual(sorted(g.adj_edges(1)), [Edge(0, 1), Edge(1, 2), Edge(1, 3)])
		self.assertEqual(sorted(g.adj_edges(2)), [Edge(0, 2), Edge(1, 2)])
		self.assertEqual(sorted(g.adj_edges(3)), [Edge(0, 3), Edge(1, 3), Edge(3, 4)])
		self.assertEqual(sorted(g.adj_edges(4)), [Edge(3, 4)])

		self.assertEqual(g.degree(0), 3)
		self.assertEqual(g.degree(1), 3)
		self.assertEqual(g.degree(2), 2)
		self.assertEqual(g.degree(3), 3)
		self.assertEqual(g.degree(4), 1)