def solve(A):
        count = 0
        i = 0
        while i < len(A):
            if A[i] == i+1:
                i+=1
            else:
                count+=1
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
        return count

A = [1, 5, 4, 3, 2] 
print(solve(A))