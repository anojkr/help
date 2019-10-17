from sys import stdin, stdout
from collections import defaultdict
import heapq, copy
import sys

def relaxation(graph, source, adj_node, weight, dest,Q):


def bellam_ford(graph, v, source):
	dest = [sys.maxsize]*v
	dest[source] = 0

	for i in range(0, v-1):
		for k, item in graph.items():
			

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

	bellam_ford(graph, V, 0)