from sys import stdin, stdout

class Node:
	def __init__(self, data):
		self.data = data
		self.nxt = None


class Linklist(Node):
	def __init__(self):
		self.head = None

	def add_node(self, data):
		"Add nodes to linklist"
		t = self.head

		if t == None:
			self.head = Node(data)
		else:
			while (t.nxt != None):
				t = t.nxt
			t.nxt = Node(data)

	def print_node(self):
		"Print linklist nodes"
		t = self.head

		if t != None:
			while t!= None:
				stdout.write(str(t.data) + " ")
				t = t.nxt
		stdout.write("\n")

	def reverse_linklist(self):
		"Reverse linklist using iterative approach"
		prev = None
		curr = self.head
		next = None

		while (curr != None):
			next = curr.nxt
			curr.nxt = prev
			prev = curr
			curr = next

		self.head = prev

	def get_head(self):
		return self.head

	def reverse_linklist_recurr(self, prev, curr):
		"Reverse a linklist using recurrsion"

		if curr == None:
			self.head = prev

		else:
			self.reverse_linklist_recurr(curr, curr.nxt)
			curr.nxt = prev

	def find_middle_element(self):
		"Find middle element in linklist"
		p1 = self.head
		p2 = self.head

		while (p2.nxt != None and p2.nxt.nxt != None):
			p1 = p1.nxt
			p2 = p2.nxt.nxt

		stdout.write(str(p1.data)+ "\n")

	def rotate_linklist(self, k):
		"Rotate a linklist by k-nodes"
		t = self.head

		while t.nxt!= None and k>1:
			t = t.nxt
			k = k - 1 
		tmp = t.nxt

		while tmp.nxt:
			tmp = tmp.nxt
		tmp.nxt = self.head
		self.head = t.nxt
		t.nxt = None

l = Linklist()
l.add_node(10)
l.add_node(20)
l.add_node(30)
l.add_node(40)
l.add_node(50)
l.add_node(60)
l.add_node(70)
l.add_node(80)
l.add_node(90)
l.add_node(100)

# l.print_node()
# head = l.get_head()
# l.reverse_linklist_recurr(None, head)
l.print_node()
# l.find_middle_element()

l.rotate_linklist(7)
l.print_node()

