//Reverse doubly linklist


def reverse(head):

	temp = None
	curr = head

	while curr!= None:
		temp = curr.next
		curr.next = prev
		curr.prev = t
		curr = curr.prev

	head = temp.prev