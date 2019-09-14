#detect directed cycle in graph using activation record method
import sys

def dfs(mat, vis, res, i):
	N = len(mat)
	vis[i] = 1
	res[i] = 1

	for adj in range(N):
		if mat[i][adj] >= 1 and vis[adj] == 0 and res[adj] == 0:
			dfs(mat, vis, res, adj)
		elif mat[i][adj] >= 1 and res[adj] == 1 and vis[adj] == 1:
			print(i,adj)
			# print(res)
			print("Cycle Detected")
	res[i] = 0

def dft(mat):
	N = len(mat)
	vis = [0]*N
	res = [0]*N

	for i in range(N):
		dfs(mat, vis, res, i)



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



 	# Cycle in graph
	# g = [[0,1,0,0,0,0],
	# 		[0,0,1,0,0,0],
	# 		[0,0,0,1,0,0],
	# 		[0,0,0,0,1,0],
	# 		[0,0,0,0,0,1],
	# 		[1,0,0,0,0,0]
	# 	]
	g = [[0,1,0,0],
 		[0,0,1,0],
 		[1,0,0,1],
 		[1,0,0,0],]

	dft(g)