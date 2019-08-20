class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    count = 0
    flag = 0
    def safe(self, matrix, visited, i, j, m, n):
        # print(i, j)
        if (i<m and j<n and i>=0 and j>=0):
            if (visited[i][j] == False and matrix[i][j] == 0):
                # print(i, j)
                self.count +=  1
                return True
        else:
            self.count -= 1 
            return False
        
    def dfs(self, matrix, visited, i, j, end_x, end_y, m, n):
        print(i, j)
        visited[i][j] = True 
        if i == end_x and j == end_y:
            # print(i, j)
            self.flag = 1
            return self.count
        else:
            a = [-1, 0, 0, 1]
            b = [0, -1, 1, 0]
            for x in range(4):
                if self.safe(matrix, visited, i+a[x], j+b[x], m, n) == True:
                    return self.dfs(matrix, visited, i+a[x], j+b[x], end_x, end_y, m, n)

        
        
    def solve(self):
        A = [ [0, 1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0],
              [0, 1, 0, 1, 1, 0],
              [1, 1, 0, 1, 1, 1],
              [1, 0, 1, 1, 0, 0],
              [1, 1, 1, 1, 1, 1],
              [0, 0, 1, 0, 1, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
        ]
        B = [ 7, 5 ]
        C = [ 8, 3 ]
        m, n = len(A), len(A[0])
        visited = [[False for j in range(n)] for i in range(m)]
        start_x, start_y = B[0], B[1]
        end_x, end_y = C[0], C[1]
        x = self.dfs(A, visited, start_x, start_y, end_x, end_y, m, n)
        if self.flag == 1:
            print(x)
            return x
        else:
            return -1



x = Solution()
x.solve()