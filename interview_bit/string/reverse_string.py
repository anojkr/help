def reverse(s, i ,j):
    start = i 
    end = j
    # print(s[i:j+1])
    while (i<j):
        t = s[i]
        s[i] = s[j]
        s[j] = t
        i+=1 
        j-=1 
    # print(s[start:end+1])
        

def solve():
    A = "Anoj Kumar Boy"
    s = list(A)
    i = 0
    n = len(s)
    j = 0
    
    
    x = 0
    y = n-1
    while x < y:
        m = s[x]
        s[x] = s[y]
        s[y] = m
        x+=1 
        y-=1 
    
    print(s)
    while j < n:
        
        while j < n and s[j]!= " ":
            j = j + 1 
        # print(A[i:j])
        reverse(s, i, j-1)
        i = j + 1
        j = j + 1
        
    print(s)
    
solve()