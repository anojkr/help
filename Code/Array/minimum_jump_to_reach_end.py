
# https://leetcode.com/problems/jump-game-ii/
# Complexity O(N)

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        # If there's no num greater than 1, than nums must be all ones, otherwise we cannot reach endpoint.
        elif max(nums)<=1:
            return len(nums)-1
        
        min_step = 0
        cur = len(nums)-1
        while True:
            for i in range(cur):
                if i + nums[i] >= cur:
                    cur = i
                    min_step += 1
                    if cur == 0:
                        return min_step
                    break