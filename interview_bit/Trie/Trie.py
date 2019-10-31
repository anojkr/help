
class Node():
	def __init__(self):
			self.is_leaf = False
			self.table = [None]*26

class Trie:
	def __init__(self):
		self.root = None

	def ordx(self, cha):
		return int(ord(cha)-ord('a'))

	def insert(self, string):
		if self.root == None:
			self.root = Node()

		temp = self.root
		for curr in string:
			idx = self.ordx(curr)
			if temp.table[idx] == None:
				temp.table[idx] = Node()
			temp = temp.table[idx]
		temp.is_leaf = True
		return True


	def search(self, string):
		temp = self.root

		for curr in string:
			idx = self.ordx(curr)
			if temp.table[idx] == None:
				return False
			temp = temp.table[idx]
		return True if temp.is_leaf == True else False


	def pattern(self, string):
		temp = self.root

		for curr in string:
			idx = self.ordx(curr)
			if temp.table[idx] == None:
				return False
			temp = temp.table[idx]
		return True if temp.is_leaf == True else False

	def empty(self,curr):
		tem = curr.table
		for x in tem:
			if x != None:
				return False
		return True

	def delete(self,curr, string, depth):

		if curr == None:
			return None

		if depth == len(string):

			if curr.is_leaf == True:
				curr.is_leaf = False

			if self.empty(curr) == True:
				del curr
				curr = None
			return curr

		idx = self.ordx(string[depth])
		curr.table[idx] = self.delete(curr.table[idx], string, depth+1)

		if (self.empty(curr) and curr.is_leaf == False):
			del curr
			curr = None
		return curr

	def remove(self, string):
		self.delete(self.root, string, 0)


def result(t):
	if t == True:
		print('string found')
	else:
		print('string not found')


if __name__ == '__main__':
	T = Trie()
	value = ["Hi", "Hello", "HelloWorld", "HiTech", "HiGeek", 
        "HiTechWorld", "HiTechCity", "HiTechLab"]
	

	for x in value:
		T.insert(x)

	# T.search("there")
	# result(T.search("the"))
	# T.remove("there")
	# result(T.search("there"))
	# result(T.search("the"))

	# result(T.search("bye"))
	# T.remove("bye")
	# result(T.search("bye"))
	print(T.root.table)
	