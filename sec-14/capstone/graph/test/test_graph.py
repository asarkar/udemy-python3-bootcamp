import capstone.graph.functions as graph
from capstone.graph.edge import Edge
from capstone.graph.undirected_graph import UndirectedGraph


class TestGraph:
    def test_no_eulerian_path(self):
        g = UndirectedGraph()
        g.add_edge(Edge(0, 1))
        g.add_edge(Edge(0, 2))
        g.add_edge(Edge(0, 3))
        g.add_edge(Edge(1, 2))
        g.add_edge(Edge(1, 3))
        g.add_edge(Edge(3, 4))

        assert not graph.eulerian_path(g)

    def test_eulerian_path(self):
        g = UndirectedGraph()
        g.add_edge(Edge(0, 1))
        g.add_edge(Edge(0, 2))
        g.add_edge(Edge(0, 3))
        g.add_edge(Edge(1, 2))
        g.add_edge(Edge(3, 4))

        assert graph.eulerian_path(g)

    def test_eulerian_circuit(self):
        g = UndirectedGraph()
        g.add_edge(Edge(0, 1))
        g.add_edge(Edge(0, 2))
        g.add_edge(Edge(0, 3))
        g.add_edge(Edge(0, 4))
        g.add_edge(Edge(1, 2))
        g.add_edge(Edge(3, 4))

        assert graph.eulerian_path(g)

    def test_dijkstra_sp(self):
        g = UndirectedGraph()
        g.add_edge(Edge(0, 1, 5))
        g.add_edge(Edge(0, 3, 9))
        g.add_edge(Edge(0, 5, 2))
        g.add_edge(Edge(1, 2, 2))
        g.add_edge(Edge(3, 4, 2))
        g.add_edge(Edge(4, 5, 3))

        (path, dist) = graph.dijkstra_sp(g, 0, 3)
        assert list(path) == [0, 5, 4, 3]
        assert dist == 7

        (path, dist) = graph.dijkstra_sp(g, 0, 2)
        assert list(path) == [0, 1, 2]
        assert dist == 7

    def test_prim_msp(self):
        g = UndirectedGraph()
        g.add_edge(Edge(0, 1, 1))
        g.add_edge(Edge(0, 3, 3))
        g.add_edge(Edge(1, 2, 1))
        g.add_edge(Edge(1, 3, 3))
        g.add_edge(Edge(2, 3, 1))

        (path, dist) = graph.prim_msp(g)
        assert len(path) == 3
        assert Edge(0, 1, 1) in path
        assert Edge(1, 2, 1) in path
        assert Edge(2, 3, 1) in path
        assert dist == 3
