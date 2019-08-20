def compare(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        t = 1 if int(ab)>int(ba) else 0
        return t

def largestNumber(nums):
        n = len(nums)
        for i in range(0, n):
            for j in range(i, n):
                res = compare(nums[i], nums[j])
                if (res == 0):
                    nums[i], nums[j] = nums[j], nums[i]
        number = "".join([str(i) for i in nums]) 
        
        return number

if __name__ == '__main__':
	arr = [3,30,34,5,9]
	print(largestNumber(arr))
