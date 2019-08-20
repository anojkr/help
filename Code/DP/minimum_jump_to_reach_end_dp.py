# https://leetcode.com/problems/jump-game/
# Complexity O(N**2)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = [sys.maxsize]*N
        
        dp[0] = 0
        for i in range(1, N):
            j = 0
            while j <= N-1 and j <= i + nums[i]:
                dp[j] = min(dp[j], dp[i]+1)
                j = j + 1
        print(dp)
        if dp[N-1] == sys.maxsize:
            return False
        else:
            return True