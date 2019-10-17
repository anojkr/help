class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lm = list(s)
        l = len(lm)
        
        r = [-1]
        for x in range(0, l):
            if r[-1] == '(' and lm[x] == ')':
                r.pop()
            elif r[-1] == '{' and lm[x] == '}':
                r.pop()
            elif r[-1] == '[' and lm[x] == ']':
                r.pop()
            else:
                r.append(lm[x])
        print(r)
                
        if len(r) == 1:
            return True 
        return False