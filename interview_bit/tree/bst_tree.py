class Node:

	def __init__(self, value):
		self.key = value
		self.left = None
		self.right = None


def inorder(root):
	if root == None:
		return root

	inorder(root.left)
	print(root.key)
	inorder(root.right)


def insert_node(root, data):
	if root == None:
			return Node(data)

	if root.key > data:
		root.left = insert_node(root.left, data)

	elif root.key < data:
		root.right = insert_node(root.right, data)

	return root

def prec(root):
	t = root
	
	while t.left.left != None:
		t = t.left

	val = root.left.key
	t.left = None
	return val


def delete(root, data):
	if root == None:
		return root

	if root.key == data:

		if root.left == None and root.right == None:
			return None

		elif root.left != None and root.right == None:
				return root.left

		elif root.left == None and root.right != None:
				return root.right

		elif root.left!= None and root.right!= None:
				t = prec(root.right)
				root.key = t

	elif root.key > data:
		root.left = delete(root.left, data)

	elif root.key < data:
		root.right = delete(root.right, data)

	return root


def search(data):
	if root == None:
		return root

	if root.key == data:
		print("element_found")
		return root

	if root.key < data:
		return search(root.left, data)

	elif root.key > data:
		return search(root.right, data)

# 8 3 10 1 6 14 4 7 13

root = Node(8)

insert_node(root, 3)
insert_node(root, 10)
insert_node(root, 1)
insert_node(root, 5)
insert_node(root, 14)
insert_node(root, 4)
insert_node(root, 7)
insert_node(root, 13)

inorder(root)
print("\n")

delete(root, 3)
# delete(root, 7)
# delete(root, 13)
inorder(root)