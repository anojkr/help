import sys
import heapq

def relax(mat, vis, des, src, adj, weight, Q):
	if des[adj] > des[src] + weight:
		des[adj] = des[src] + weight
		t = des[adj]
		heapq.heappush(Q, (t, adj))

def distra(mat, source, N):
	vis = [0]*N 
	des = [sys.maxsize]*N
	vis[source] = 1
	des[source] = 0
	Q = []
	Q.append((0, source))
	heapq.heapify(Q)

	
	while len(Q)>0:
		dest, src = heapq.heappop(Q)
		vis[src] = 1

		for adj in range(N):
			if mat[src][adj] != 0 and vis[adj] == 0:
				relax(mat, vis, des, src, adj, mat[src][adj], Q)

	print(des)

if __name__ == '__main__':
	g	=		[[0, 4, 0, 0, 0, 0, 0, 8, 0],
				[4, 0, 8, 0, 0, 0, 0, 11, 0],
				[0, 8, 0, 7, 0, 4, 0, 0, 2],
				[0, 0, 7, 0, 9, 14, 0, 0, 0],
				[0, 0, 0, 9, 0, 10, 0, 0, 0],
				[0, 0, 4, 14, 10, 0, 2, 0, 0],
				[0, 0, 0, 0, 0, 2, 0, 1, 6],
				[8, 11, 0, 0, 0, 0, 1, 0, 7],
				[0, 0, 2, 0, 0, 0, 6, 7, 0]]
	N = len(g)
	distra(g, 0, N)