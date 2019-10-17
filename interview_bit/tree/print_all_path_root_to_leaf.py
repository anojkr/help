
First approach

res = []

def solve(root, res):
	if root == None:
		return
	res.append(root.val)
	
	self.solve(root.left)
	
	if root.left == None and root.right == None:
		print(res)
	
	self.solve(root.right)
	res.pop()





# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    
    def solve(self, A, B, res, result):
        if A == None:
            return 
        
        res.append(A.val)
        
        if A.left == None and A.right == None:
            if sum(res) == B:
                s = copy.deepcopy(res)
                result.append(s)
        self.solve(A.left, B, res, result)
        self.solve(A.right, B, res, result)
        res.pop()
    
    def pathSum(self, A, B):
        if A == None:
            return 
        res = []
        result = [] 
        self.solve(A, B, res, result)
        # print(result)
        return result
