
def find_duplicate(head):
	
	if head == None and head.next = None:
		return head

	curr = head
	prev = None

	while curr!= None:
		if curr.data in h:
			t = curr
			curr = curr.next
			prev.next = curr
			free(t)
			continue
		else:
			h[curr.data] = 1
			prev = curr
			curr = curr.next
