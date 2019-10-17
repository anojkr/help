def dfs(mat, vis, stack, i):
	vis[i] = 1
	for adj in range(len(mat)):
		if vis[adj] == 0 and mat[i][adj] == 1:
			dfs(mat, vis, stack, adj)
	stack.append(i)


def topological_sort(mat):
	N = len(mat)
	vis = [0]*N
	stack = []

	for i in range(N):
		if vis[i] == 0:
			dfs(mat, vis, stack, 0)

	print(stack)
	print(vis)

if __name__ == '__main__':
	g = [[0,1,1,1,0,0,0],
		 [0,0,0,0,1,0,0],
		 [0,0,0,0,1,0,0],
		 [0,0,0,0,1,1,0],
		 [0,0,0,0,0,0,1],
		 [0,0,0,0,0,0,1],
		 [0,0,0,0,0,0,0]]

	topological_sort(g)
