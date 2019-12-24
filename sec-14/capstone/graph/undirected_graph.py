from typing import Set
from .edge import Edge
from functools import wraps


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

    def _has_vertex(method):
        @wraps(method)
        def wrap(self, *args, **kwargs):
            if args[0] not in self.adj:
                return None
            return method(self, *args, **kwargs)

        return wrap

    @_has_vertex
    def adj_edges(self, v: int) -> Set[Edge]:
        return self.adj[v]

    @_has_vertex
    def degree(self, v: int) -> int:
        return len(self.adj[v])

    def __repr__(self) -> str:
        return f"{self.adj}"
