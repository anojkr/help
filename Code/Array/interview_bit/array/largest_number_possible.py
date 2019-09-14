class Solution:
    # @param A : tuple of integers
    # @return a strings

    def largestNumber(self, A):

        array = list(A)
        l = len(str(max(array))) + 1
        res= []
        for i in array:
            temp = str(i)*l
            res.append((temp[:l], i))
        res.sort(reverse=True)
        
        s = ""
        for i in res:
            s = str(s) + str(i[1])
        return int(s)

                
