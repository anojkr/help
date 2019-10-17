from sys import stdin, stdout
import copy
from collections import defaultdict

def dfs(graph_list, visited, r,  topnum, trace, i):
	visited[i] = 1
	if i in graph_list:
		for adj in graph_list[i]:
			if visited[adj[0]] == 0:
				r.append(adj[0])
				x = dfs(graph_list, visited, r, topnum, trace, adj[0])
				topnum.append((x, adj[0]))
		trace[0] -= 1
	return trace[0]

def topological_sort(graph_list, n):
	visited = [0]*n
	r = []
	trace = [n]
	topnum = []
	for i, item in graph_list.items():
		if visited[i] == 0:
			r.append(i)
			x = dfs(graph_list, visited, r, topnum , trace, i)
			topnum.append((x, i))
		trace[0]-=1
	print(r)
	# print(topnum)
	topnum.sort()
	print(topnum)
	# for tag, node in topnum:
	# 	print(tag)

def convert_matrix_list(graph):
	d = defaultdict(list)

	for i in range(0, len(graph)):
		for j in range(0,len(graph)):
			if graph[i][j] != 0:
				d[i].append((j, graph[i][j]))
	return d



if __name__ == '__main__':
	# g = 	[	   [0, 4, 0, 0, 0, 0, 0, 8, 0], 
 #                   [4, 0, 8, 0, 0, 0, 0, 11, 0], 
 #                   [0, 8, 0, 7, 0, 4, 0, 0, 2], 
 #                   [0, 0, 7, 0, 9, 14, 0, 0, 0], 
 #                   [0, 0, 0, 9, 0, 10, 0, 0, 0], 
 #                   [0, 0, 4, 14, 10, 0, 2, 0, 0], 
 #                   [0, 0, 0, 0, 0, 2, 0, 1, 6], 
 #                   [8, 11, 0, 0, 0, 0, 1, 0, 7], 
 #                   [0, 0, 2, 0, 0, 0, 6, 7, 0]
 #            ]
	# graph for check connected components	]
	# g = [	[0,1,0,0,0,0],
	# 		[1,0,0,0,0,0],
	# 		[0,0,0,1,0,0],
	# 		[0,0,1,0,0,0],
	# 		[0,0,0,0,0,1],
	# 		[0,0,0,0,1,0]
	# 	]

	# Cycle in graph
	# g = [[0,1,0,0,0,0],
	# 		[0,0,1,0,0,0],
	# 		[0,0,0,1,0,0],
	# 		[0,0,0,0,1,0],
	# 		[0,0,0,0,0,1],
	# 		[1,0,0,0,0,0]
	# 	]


	# g = [	[0,1,0,0,0],
	# 		[0,0,1,0,0],
	# 		[0,0,0,1,0],
	# 		[0,0,0,0,1],
	# 		[0,0,0,0,0]
	# 	]
	g = [	[0,1,1,1,0,0,0,0,0],
		[0,0,0,0,1,0,0,0,0],	
		[0,0,0,0,1,1,1,0,0],
		[0,0,0,0,0,0,1,1,0],
		[0,0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,0,0,1],
		[0,0,0,0,0,0,0,0,0]]

	graph_list = convert_matrix_list(g)

	print(graph_list)

	topological_sort(graph_list, 9)





