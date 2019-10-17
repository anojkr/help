class Solution:
    
    def safe(self, grid, matrix, i, j, m, n):
        if (i < m and j < n and i >= 0 and j >=0):
            if ( grid[i][j] == '1' and matrix[i][j] == False):
                return True
        else:
            return False
    
    def dfs(self, grid, matrix, i, j, m, n):
        matrix[i][j] = True
        # a = [-1, -1, -1, 0, 0, 1, 1, 1]
        # b = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        a = [-1, 0, 0, 1]
        b = [0, -1, 1, 0]
        
        for x in range(4):
            if self.safe(grid, matrix, i+a[x], j + b[x], m, n) == True:
                    self.dfs(grid, matrix, i + a[x], j + b[x], m, n)
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        
        matrix = [[False for j in range(n)]for i in range(m)]
        count = 0
        
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == '1' and matrix[i][j] == False:
                    self.dfs(grid, matrix, i, j, m, n)
                    count += 1
        return count
        
    