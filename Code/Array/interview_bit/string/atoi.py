

class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, s):
        s = s.strip() # strips all spaces on left and right
        if not s: return 0
        sign = -1 if s[0] == '-' else 1
        val, index = 0, 0
        if s[0] in ['+', '-']: index = 1
        while index < len(s) and s[index].isdigit():
            val = val*10 + ord(s[index]) - ord('0') # assumes there're no invalid chars in given string
            index += 1
        #return sign*val
        return max(-2**31, min(sign * val,2**31-1))

