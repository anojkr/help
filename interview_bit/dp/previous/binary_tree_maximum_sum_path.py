class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        final=[-100000000]
        def recursion(node,final):
            if(node==None):
                return 0
            else:
                a=recursion(node.left,final)
                b=recursion(node.right,final)
                val=final[0]
                final.pop()
                final.append(max(val,a+b+node.val))
                return max(max(a,b)+node.val,0)
        recursion(A,final)
        return final[0]