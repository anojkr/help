class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)-1
        s = sum(nums)
        print(s)
        s = s/2.0
        k = []
        
        nums.sort()
        t = 0
        for i in range(N, -1, -1):
            if t + nums[i] - s <= 0:
                k.append(nums[i])
                t = t+nums[i]
        print(k)
        print(t)
        print(s)
        if sum(k) == s:
            return True
        else:
            return False