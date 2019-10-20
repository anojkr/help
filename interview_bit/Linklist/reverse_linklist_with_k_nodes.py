
def reverse(head, k):

	prev = None
	curr = head
	next_node = None

	c = 0
	
	while (curr!= None and c < k):
		
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
		c = c + 1

	if next_node!= None:
		head.next = reverse(next_node, k)

	return prev