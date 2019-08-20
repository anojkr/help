# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# complexity O(N)

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        
        c = 0
        for i in range(1, min(l1, l2)+1):
                m = l1//i
                if l1%i == 0 and l2%i == 0:
                    if str1 == str2[0:i]*m:
                        c = i
        return str2[:c]