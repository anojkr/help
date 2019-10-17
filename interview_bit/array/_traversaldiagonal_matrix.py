
def solve():
    
    A = [   [1 , 2 , 3 , 4],
            [5 , 6 , 7 , 8],
            [9 , 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20]]
            
    m = len(A)
    n = len(A[0])
    
    for z in range(0, m):
        i = z
        j = 0
        res = []
        while i >=0 and j < n:
            res.append(A[i][j])
            i-=1
            j+=1
        print(res)
        
    for z in range(1, n):
        i = m-1
        j = z
        res = []
        
        while i >= 0 and j<n:
            res.append(A[i][j])
            i = i-1
            j = j+1
        print(res)
solve()