# asarkar:sec-14$ python -m unittest discover

import unittest
import undirected_graph as ug

class TestUndirectedGraph(unittest.TestCase):
	def test_init(self):
		g = ug.UndirectedGraph()
		self.assertEqual(len(g.vertices()), 0)

	def test_graph(self):
		g = ug.UndirectedGraph()
		g.add_edge(ug.Edge(0, 1))
		g.add_edge(ug.Edge(0, 2))
		g.add_edge(ug.Edge(0, 3))
		g.add_edge(ug.Edge(1, 2))
		g.add_edge(ug.Edge(1, 3))
		g.add_edge(ug.Edge(3, 4))

		self.assertEqual(sorted(g.vertices()), list(range(5)))

		self.assertEqual(sorted(g.adj_edges(0)), [ug.Edge(0, 1), ug.Edge(0, 2), ug.Edge(0, 3)])
		self.assertEqual(sorted(g.adj_edges(1)), [ug.Edge(0, 1), ug.Edge(1, 2), ug.Edge(1, 3)])
		self.assertEqual(sorted(g.adj_edges(2)), [ug.Edge(0, 2), ug.Edge(1, 2)])
		self.assertEqual(sorted(g.adj_edges(3)), [ug.Edge(0, 3), ug.Edge(1, 3), ug.Edge(3, 4)])
		self.assertEqual(sorted(g.adj_edges(4)), [ug.Edge(3, 4)])

		self.assertEqual(g.degree(0), 3)
		self.assertEqual(g.degree(1), 3)
		self.assertEqual(g.degree(2), 2)
		self.assertEqual(g.degree(3), 3)
		self.assertEqual(g.degree(4), 1)