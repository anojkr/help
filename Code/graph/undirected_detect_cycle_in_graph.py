#Detect cycle in undireced graph using parent method
def dfs(mat, vis, par, p, i):

	vis[i] = 1
	par[i] = p
	for adj in range(len(mat)):
		if vis[adj] == 1 and par[adj] != i and mat[i][adj] >= 1:
			print("cycle_detected")
			print(i, adj)
			return 
		if vis[adj] == 0 and mat[i][adj] >= 1:
			return dfs(mat, vis, par, i, adj)

def dft(mat):
	N = len(mat)

	vis = [0]*N
	par = {}
	for i in range(N):
		if vis[i] == 0:
			dfs(mat, vis, par, -1, i)
	print(par)

if __name__ == '__main__':
	# Cycle in graph
	# g = [[0,1,0,0,0,0],
	# 		[0,0,1,0,0,0],
	# 		[0,0,0,1,0,0],
	# 		[0,0,0,0,1,0],
	# 		[0,0,0,0,0,1],
	# 		[1,0,0,0,0,0]
	# 	]

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
	g = [[0,1,0,0],
 		[0,0,1,0],
 		[1,0,0,1],
 		[1,0,0,0],]
	dft(g)