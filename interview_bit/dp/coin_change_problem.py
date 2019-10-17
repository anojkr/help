
# Complete the getWays function below.
def getWays(n, c):

    m = len(c)
    table = [[int(-1) for y in range(n+1)] for x in range(m+1)]

    for j in range(0, n+1):
        table[0][j] = 0
    for i in range(0, m+1):
        table[i][0] = 1

    for i in range(1, m+1):
        for j in range(1, n+1):
            if j >= c[i-1]:
                table[i][j] = table[i-1][j] + table[i][j-c[i-1]]
            else:
                table[i][j] = table[i-1][j]


    return table[m][n]

