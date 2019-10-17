
def solve():
    
    A = [   [1 , 2 , 3 , 4],
            [5 , 6 , 7 , 8],
            [9 , 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20]]
        # [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]
    m = len(A)
    n = len(A[0])
    
    i = 0 
    j = 0 
    l = m-1
    c = n-1
    flag = 0
    t = 0
    res = []
    while i < l and j < c:
        for k in range(j, c+1):
            # print(A[i][k])
            res.append(A[i][k])
        i+=1
        
        for k in range(i, l+1):
            # print(A[k][c])
            res.append(A[k][c])
        c-=1
        
        for k in range(c, j-1, -1):
            res.append(A[l][k])
        l-=1
        
        for k in range(l, i-1, -1):
            # print(A[k][j])
            res.append(A[k][j])
        j+=1
    print(res)
    
solve()