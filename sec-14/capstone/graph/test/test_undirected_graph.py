from capstone.graph.edge import Edge
from capstone.graph.undirected_graph import UndirectedGraph


class TestUndirectedGraph:
    def test_init(self):
        g = UndirectedGraph()
        assert len(g.vertices()) == 0

    def test_graph(self):
        g = UndirectedGraph()
        g.add_edge(Edge(0, 1))
        g.add_edge(Edge(0, 2))
        g.add_edge(Edge(0, 3))
        g.add_edge(Edge(1, 2))
        g.add_edge(Edge(1, 3))
        g.add_edge(Edge(3, 4))

        assert sorted(g.vertices()) == list(range(5))

        assert sorted(g.adj_edges(0)) == [Edge(0, 1), Edge(0, 2), Edge(0, 3)]
        assert sorted(g.adj_edges(1)) == [Edge(0, 1), Edge(1, 2), Edge(1, 3)]
        assert sorted(g.adj_edges(2)) == [Edge(0, 2), Edge(1, 2)]
        assert sorted(g.adj_edges(3)) == [Edge(0, 3), Edge(1, 3), Edge(3, 4)]
        assert sorted(g.adj_edges(4)) == [Edge(3, 4)]

        assert g.degree(0) == 3
        assert g.degree(1) == 3
        assert g.degree(2) == 2
        assert g.degree(3) == 3
        assert g.degree(4) == 1

        assert g.adj_edges(100) is None
        assert g.degree(100) is None
