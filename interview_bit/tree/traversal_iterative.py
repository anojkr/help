

def pre_solve(root)
	
	p = root
	res = []
	while True:

		while(p != None){
			print(p.val)
			stack.append(p.val)
			p = p.left
		}

		if len(res) == 0:
			break

		p = res.pop()
		p = p.right

def inorder_solve(root)
	
	p = root
	res = []
	while True:

		while(p != None){
			# print(p.val)
			stack.append(p.val)
			p = p.left
		}

		if len(res) == 0:
			break

		p = res.pop()
		print(p.val)
		p = p.right

