
Diameter of binary tree

def height(root):
	
	if root == None:
		return 0

	l = self.height(root.left)
	r = self.height(root.right)

	return 1 + max(l, r)


def diameter(root):
	if root == None:
		return 0

	l = self.height(root.left)
	r = self.height(root.right)

	ld = self.diameter(root.left)
	rd = self.diameter(root.right) 

	return max(1+l+r, max(ld, rd))