from sys import stdin, stdout

def longest_common_subsequence_solve(X, Y, len_x, len_y):
    mat = [[int(0) for y in range(len_x+1)] for x in range(len_y+1)]
    
    for i in range(1, len_y+1):
        for j in range(1, len_x+1):
            if Y[i-1] == X[j-1]:
                mat[i][j] = 1 + mat[i-1][j-1]
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])
    print(mat)
    print(mat[len_y][len_x])
        

if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    len_x = len(X)
    len_y = len(Y)
    longest_common_subsequence_solve(X, Y, len_x, len_y)
    