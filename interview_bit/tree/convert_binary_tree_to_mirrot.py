
def mirror(root):
	if root == None:
		return 

	self.mirror(root.left)
	self.mirror(root.right)

	t = root.left
	root.left = root.right
	root.right = t
	