from sys import stdin, stdout
from collections import defaultdict
import heapq, copy
import sys

def relaxation(graph, source, adj_node, weight, dest,Q):
	if dest[adj_node] > dest[source] + weight:
		t =  dest[source] + weight
		dest[adj_node] = t
		heapq.heappush(Q, (t, adj_node))

def dijstra(graph, v, source):
	dest = [sys.maxsize]*v
	visited = [0]*v
	dest[source] = 0
	Q = []
	Q.append((0, source))
	heapq.heapify(Q)

	while len(Q)>0:
		u = heapq.heappop(Q)
		src = u[1]
		visited[src] = 1
		for i in range(0, len(graph[src])):
				adj = graph[src][i]
				adj_node, weight = adj
				if visited[adj_node] == 0 :
					relaxation(graph, src, adj_node, weight, dest, Q)
	print(dest)



if __name__ == '__main__':

	# V, E = stdin.readline().split()
	graph = defaultdict(list)
	g = 	[	   [0, 4, 0, 0, 0, 0, 0, 8, 0], 
                   [4, 0, 8, 0, 0, 0, 0, 11, 0], 
                   [0, 8, 0, 7, 0, 4, 0, 0, 2], 
                   [0, 0, 7, 0, 9, 14, 0, 0, 0], 
                   [0, 0, 0, 9, 0, 10, 0, 0, 0], 
                   [0, 0, 4, 14, 10, 0, 2, 0, 0], 
                   [0, 0, 0, 0, 0, 2, 0, 1, 6], 
                   [8, 11, 0, 0, 0, 0, 1, 0, 7], 
                   [0, 0, 2, 0, 0, 0, 6, 7, 0] 
            ]
	V = len(g)
	Q = []
	for source in range(0, V):
		for destination in range(0, V):
			if g[source][destination] != 0:
				graph[source].append((destination, g[source][destination]))
				Q.append((g[source][destination], source, destination))

	dijstra(graph, V, 0)