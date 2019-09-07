from sys import stdin, stdout
from collections import defaultdict
import heapq, copy
import sys
import copy

def calculation(matrix, v):
	temp_1 = copy.deepcopy(matrix)  
	temp_2 = copy.deepcopy(matrix)  
	for k in range(0,v):
		temp_1 = copy.deepcopy(temp_2)  
		for i in range(0, v):
			for j in range(0, v):
				if i != j:
					temp_2[i][j] = min(temp_1[i][j], temp_1[i][k] + temp_1[k][j])

	for i in range(0, v):
		for j in range(0, v):
			if temp_1[i][j] == sys.maxsize:
				temp_1[i][j] = 0
	for x in temp_1:
		print(x)

def warshall(graph, v, source):
	matrix = [[sys.maxsize for y in range(0, v)] for x in range(0, v)]
	for k, item in graph.items():
		for i, w in item:
			matrix[k][i] = w
	calculation(matrix, v)



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

	warshall(graph, V, 0)