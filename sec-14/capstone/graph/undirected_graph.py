from typing import Set

from .edge import Edge


class UndirectedGraph:
    def __init__(self):
        self.adj = dict()

    def vertices(self) -> Set[int]:
        return set(self.adj.keys())

    def add_edge(self, e: Edge) -> None:
        if e.tail not in self.adj:
            self.adj[e.tail] = set()
        if e.head not in self.adj:
            self.adj[e.head] = set()

        self.adj[e.head].add(e)
        self.adj[e.tail].add(e)

    def adj_edges(self, v: int) -> Set[Edge]:
        if v not in self.adj:
            return None
        return self.adj[v]

    def degree(self, v: int) -> int:
        if v not in self.adj:
            return None
        return len(self.adj[v])

    def __repr__(self) -> str:
        return f"{self.adj}"
