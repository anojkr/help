binary_tree_subtree_of_another_binary_tree


def is_identical(self, root, t):
	if root == None and t == None:
		return True
	if root != None and t != None:
		return (root.val == t.val and self.is_identical(root.left, t.left) and
				self.is_identical(root.right, t.right))

	return 0

def solve(root, t):
	if t ==  None:
		return True

	if root == None:
		return False

	if self.is_identical(root, t) == True:
		return True

	return self.solve(root.left, t) or self.solve(root.right, t)
