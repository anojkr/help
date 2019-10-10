# cook your dish here
def solve():
    # Output  = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10, 11, 12, 16, 15, 14, 13, 17, 18, 19, 20]
    A = [   [1 , 2 , 3 , 4],
            [5 , 6 , 7 , 8],
            [9 , 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20]]

    m = len(A)
    n = len(A[0])
    
    flag = 0
    i = 0
    res = []
    while i < m:
        
        if flag == 0:
            for j in range(0, n):
                res.append(A[i][j])
            flag = 1
        elif flag == 1:
            for j in range(n-1, -1, -1):
                res.append(A[i][j])
            flag = 0
        i+=1
    print(res)
solve()