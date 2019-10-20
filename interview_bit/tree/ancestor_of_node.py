
def solve(root, data):

	if root == None:
		return False

	if root.key == data:
		retur True

	l = solve(root.left, data)
	r = solve(root.right, data)

	if l == True or r == True:
		print(root.data)
		return True

	return False