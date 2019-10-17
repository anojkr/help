

def solve(root, k):
	if root == None:
		return

	if k == 0:
		print(root.val)

	self.solve(root.left, k-1)
	self.solve(root.right, k-1)