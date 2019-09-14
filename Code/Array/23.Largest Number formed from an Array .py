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

                




# def compare(a, b):
#         ab = str(a) + str(b)
#         ba = str(b) + str(a)
#         t = 1 if int(ab)>int(ba) else 0
#         return t

# def largestNumber(nums):
#         n = len(nums)
#         for i in range(0, n):
#             for j in range(i, n):
#                 res = compare(nums[i], nums[j])
#                 if (res == 0):
#                     nums[i], nums[j] = nums[j], nums[i]
#         number = "".join([str(i) for i in nums]) 
        
#         return number

# if __name__ == '__main__':
# 	arr = [3,30,34,5,9]
# 	print(largestNumber(arr))
