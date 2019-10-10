# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def minDepth(self, root):
        if root is None: 
            return 0 

        if root.left is None and root.right is None: 
            return 1

        if root.left is None: 
            return self.minDepth(root.right)+1

        if root.right is None: 
            return self.minDepth(root.left) +1 
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
