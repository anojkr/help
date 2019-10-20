class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        k = B
        c = 0
        n = len(A)
        freq = [0]*k
        
        for i in range(0, n):
            freq[A[i]%k]+=1

        i = 1
        j = k-1
        
        save = 0
        save = freq[0]*(freq[0]-1)//2
        
        while i < j :
                if freq[i] > 0 and freq[j] > 0:
                    save = save + freq[i]*freq[j]
                i+=1
                j-=1
                
        if k%2 == 0:
            save += (freq[B // 2] * (freq[B // 2] - 1) / 2);

        return int(save)
