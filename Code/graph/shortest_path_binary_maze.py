import sys
def is_safe(mat, vis, x, y):
	M = len(mat)
	N = len(mat[0])

	if (x >= 0  and x < M and y >=0 and y < N  and mat[x][y] == 1 and vis[x][y] == 0 ):
		return True
	return False


def shortest_path(mat, vis, x, y, end_x, end_y, min_dist, dist):

	if (x == end_x  and y == end_y):
		min_dist[0] = min(min_dist[0], dist)
		print(min_dist[0])
		for x in vis:
			print(x)
		print('\n')
		return 

	vis[x][y] = 1
	a = [0,-1,0,1]
	b = [-1,0,1,0]

	for i in range(0, len(a)):
		if is_safe(mat, vis, x+a[i], y+b[i]):
			shortest_path(mat, vis, x+a[i], y+b[i], end_x, end_y, min_dist, dist+1)
	vis[x][y] = 0



if __name__ == '__main__':
	mat = 	[ [ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
		[ 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 ],
		[ 0, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
		[ 1, 0, 1, 1, 1, 0, 1, 1, 0, 1 ],
		[ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1 ],
		[ 1, 0, 1, 1, 1, 0, 0, 1, 1, 0 ],
		[ 0, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
		[ 0, 1, 1, 1, 1, 1, 1, 1, 0, 0 ],
		[ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
		[ 0, 0, 1, 0, 0, 1, 1, 0, 0, 1 ],
	]

	M = len(mat)
	N = len(mat[0])

	vis = [[0 for j in range(N)]for i in range(M)]
	min_dist = [sys.maxsize]

	shortest_path(mat, vis, 0, 0, 9, 9, min_dist, 0)
	print(min_dist[0])
	# print(vis)