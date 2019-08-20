from sys import stdin, stdout
import copy
from collections import defaultdict

def dfs_matrix(graph_matrix, visited, v, i, traverse):
	visited[i] = 1
	for adj in range(0, v):
		if graph_matrix[i][adj] != 0 and visited[adj] == 0:
			traverse.append(adj)
			dfs_matrix(graph_matrix, visited, v, adj, traverse)

def dft_matrix(graph_matrix):
	v = len(graph_matrix)
	visited = [0]*v
	c = 0
	r = []
	for i in range(0, v):
		if visited[i] == 0:
			traverse = []
			c += 1
			traverse.append(i)
			dfs_matrix(graph_matrix, visited, v, i, traverse)
			r.append(traverse)
	return c, r


def dfs_list(graph_list, visited, v, i, traverse):
	visited[i] = 1
	for adj in graph_list[i]:
		#adj = (destination, weight)
		if visited[adj[0]] == 0:
			traverse.append(adj[0])
			dfs_list(graph_list, visited, v, adj[0], traverse)

def dft_list(graph_list):
	v = len(graph_list)
	visited = [0]*v
	c = 0
	r = []

	for i, item in graph_list.items():
		if visited[i] == 0:
			traverse = []
			c +=1
			traverse.append(i)
			dfs_list(graph_list, visited, v, i, traverse)
			r.append(traverse)	
	return c, r


def dfs_detect_cycle(graph_list, visited, parent, v, i, traverse):
	visited[i] = 1
	for adj in graph_list[i]:
		parent = i
		if visited[adj[0]] == 0 and adj[0] != parent:
			traverse.append(adj[0])
			return dfs_detect_cycle(graph_list, visited, parent, v, adj[0], traverse)
		else:
			traverse.append(adj[0])
			return True



def detect_cycle_list(graph_list):
	v = len(graph_list)
	visited = [0]*v
	parent = -1
	res = []
	for i in range(0, v):
		traverse = []
		if visited[i] == 0:
			traverse.append(i)
			r = dfs_detect_cycle(graph_list, visited,parent,  v, i, traverse)
			res.append(traverse)
			if r == True:
				print(traverse)
				print("Cycle Detected")
	print(res)

def check_color(color, parent, child):
	if color[parent] == color[child]:
		return False
	else:
		return True

def put_color(color, parent, child):
	if color[parent] == 5:
		color[child] = 10
	else:
		color[child] = 5

def dfs_bipartile(graph_list, visited, color, parent, child):
	visited[child] = 1
	put_color(color, parent, child)
	for adj in graph_list[child]:
		r = check_color(color, child, adj[0])
		if r == False:
			return False
		elif visited[adj[0]] == 0:
			return dfs_bipartile(graph_list, visited, color, child, adj[0])
	return True



def check_bipartile_list(graph_list, source):
	v = len(graph_list)
	visited = [0]*v
	color = [0]*v
	visited[source] = 1
	color[source] = 5

	for adj in graph_list[source]:
		destination = adj[0]
		if visited[destination] == 0:
			return dfs_bipartile(graph_list, visited, color, source, destination)
	# print(visited)
	

def convert_matrix_list(graph):
	d = defaultdict(list)

	for i in range(0, len(graph)):
		for j in range(0,len(graph)):
			if graph[i][j] != 0:
				d[i].append((j, graph[i][j]))
	return d

def convert_list_matrix(graph_list):
	matrix = [[0 for j in range(len(graph_list))]for i in range(len(graph_list))]
	for i, item in graph_list.items():
		for j, w in item:
			matrix[i][j] = w
	return matrix


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


	g = [	[0,1,0,0,0],
			[0,0,1,0,0],
			[1,0,0,0,0],
			[0,0,0,0,1],
			[0,0,0,1,0]
		]

	graph_list = convert_matrix_list(g)
	graph_matrix = convert_list_matrix(graph_list)
	# print(graph_list)
	print(graph_matrix)

	# no_of_component, traverse_matrix_list = dft_matrix(graph_matrix)
	# print(no_of_component)
	# print(traverse_matrix_list)


	no_of_component_list, traverse_list = dft_list(graph_list)
	# print(no_of_component_list)
	# print(traverse_list)

	detect_cycle_list(graph_list)


	# print(check_bipartile_list(graph_list, 0))



