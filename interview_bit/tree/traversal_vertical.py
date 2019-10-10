
from collection import defaultdict

def solve(root, index, d)
	if root == None:
		return

	d[index].append(root.val)
	self.solve(root.left, index-1, d)
	self.solve(root.right, index+1, d) 


d = defaultdict(list)
solve(root, 0, d)