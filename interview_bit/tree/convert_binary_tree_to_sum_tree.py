
Convert binary tree to sumtree

def solve(root):

	if root == None:
		return 0

	l = self.solve(root.left)
	r = self.solve(root.right)

	old_data  = root.data
	root.data = l+r

	return root.data  + old_data