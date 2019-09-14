class Solution:
    # @param A : list of list of integers
    # @return an integer
    
    count = 0
    def safe(self, A, vis, i, j):
        if i >=0 and i < len(A) and j >=0 and j < len(A[0]):
            if vis[i][j] == 0 and A[i][j] == 0:
                return True
        return False
    
    def dfs(self, A, vis, i, j, end_x, end_y):
        # print(i, j)
        if i == end_x and j == end_y:
            # print(vis)
            self.count+=1
            return 
        
        vis[i][j] = 1
        a = [0, 1]
        b = [1, 0]
        
        for k in range(len(a)):
            if self.safe(A, vis, i+a[k], j+b[k]):
                self.dfs(A, vis, i+a[k], j+b[k], end_x, end_y)
        vis[i][j] = 0

                
        
    def uniquePathsWithObstacles(self, A):
        
        n1 = len(A)
        n2 = len(A[0])

        if A[0][0] == 1 or A[n1-1][n2-1] == 1:
            return 0
        
        if n1 == 1 and n2 == 1:
            return 1
            
        vis = [[0 for j in range(n2)] for i in range(n1)]
        self.dfs(A, vis, 0, 0 , n1-1, n2-1)
        return self.count
