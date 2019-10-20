
def middle(head):
	
	if head == None or head.next == None:
		return None

	slow = head
	fast = head

	while fast!=None or fast.next !=None:
		fast =fast.next.next
		slow = slow.next

	return slow.data
