https://www.youtube.com/watch?v=hrTkPguJC8E

Level of node


def solve(root, target, level):
	if root == None:
		return 0

	if root.val == target:
		return level

	l = solve(root.left, target, level+1)
	if l!= 0:
		return l
	else:
		return solve(root.right, target, level+1)
