import collections
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, grid):
        Q=collections.deque([])
        n=len(grid)
        m=len(grid[0])
        cnt=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]==1):
                    cnt+=1
                if(grid[i][j]==2):
                    Q.append((i,j))
        res=0
        while Q:
            for _ in range(len(Q)):
                i,j=Q.popleft()
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if(0<=x<n and 0<=y<m and grid[x][y]==1):
                        grid[x][y]=2
                        cnt-=1
                        Q.append((x,y))
            res+=1
        if cnt==0:
            return max(0,res-1)
        else:
            return -1

