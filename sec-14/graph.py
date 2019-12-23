import undirected_graph as ug
from collections import deque
import math
import heapq
from typing import Set, Deque

# https://www.youtube.com/watch?v=xR4sGgwtR2I
# https://www.youtube.com/watch?v=8MpoO2zA2l4
def eulerian_path(g: ug.UndirectedGraph) -> Deque[int]:
	degrees = dict(map(lambda v: (v, g.degree(v)), g.vertices()))
	odd_degrees = list(filter(lambda kv: kv[1] % 2 != 0, degrees.items()))

	start = None
	if len(odd_degrees) == 0: # Eulerian circuit
		start = g.vertices()[0]
	elif len(odd_degrees) == 2: # Eulerian path
		start = odd_degrees[0][0]
	else:
		return None

	visited = set()
	path = deque()

	def __dfs(v: int, u: int = None) -> None:
		if u is not None:
			visited.add(ug.Edge(u, v))

		for x in filter(lambda e: e not in visited, g.adj_edges(v)):
			degrees[v] -= 1
			degrees[x.other(v)] -= 1
			__dfs(x.other(v), v)

		# if no more unvisited edges, add to path and backtrack
		if degrees[v] == 0:
			path.appendleft(v)

	__dfs(start)

	return path

	# run DFS and if visited == g.vertices(), graph is connected
def is_connected(g: ug.UndirectedGraph) -> bool:
	pass

# https://www.youtube.com/watch?v=lAXZGERcDf4
def dijkstra_sp(g: ug.UndirectedGraph, src: int, target: int) -> (Deque[int], int):
	unexplored = []
	parent = dict()
	dist = dict()
	visited = set()

	heapq.heappush(unexplored, (0, src, None))

	while unexplored:
		(d, v, u) = heapq.heappop(unexplored)

		# heapq doesn't have decrease key or contains operations, so we potentially add
		# duplicate vertices to the heap, and keep track of visited vertices seperately. the
		# first time a vertex is popped from the heap, its distance is the minimum; subsequent
		# retrievals of the same vertex are ignored
		if v not in visited:
			visited.add(v)
			dist[v] = d
			parent[v] = u

			if v == target:
				break
			for e in filter(lambda x: x.other(v) not in visited, g.adj_edges(v)):
				heapq.heappush(unexplored, (e.weight + d, e.other(v), v))

	path = deque()
	x = target
	while x != src:
		path.appendleft(x)
		x = parent[x]

	path.appendleft(src)

	return (path, dist[target])

# https://www.youtube.com/watch?v=oP2-8ysT3QQ
# To implement Kruskal's algorithm, we need a Union-Find data structure. Following are couple of implementations.
# https://www.nayuki.io/page/disjoint-set-data-structure
# https://github.com/mrapacz/disjoint-set
def prim_msp(g: ug.UndirectedGraph) -> (Set[ug.Edge], int):
	unexplored = []
	visited = set()
	path = set()
	sum = 0

	heapq.heappush(unexplored, (0, 0, None))

	while unexplored:
		(_, v, e) = heapq.heappop(unexplored)

		if v not in visited:
			visited.add(v)
			if e is not None:
				path.add(e)
				sum += e.weight

			for y in filter(lambda x: x.other(v) not in visited, g.adj_edges(v)):
				heapq.heappush(unexplored, (y.weight, y.other(v), y))

	return (path, sum)



