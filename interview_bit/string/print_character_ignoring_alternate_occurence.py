# cook your dish here
from collections import defaultdict
def solve():
    A = "It is a long day Dear"
    h = defaultdict()
    n = len(A)
    res = []
    
    for i in range(0, n):
        t = A[i].lower()
        if t in h:
            h[t] +=1
        else:
            h[t] = 1
        
        if h[t]%2 == 1:
            # print(A[i])
            res.append(A[i])
    print("".join(map(str, res)))
solve()