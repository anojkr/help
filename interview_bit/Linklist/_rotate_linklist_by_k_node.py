

def rotate(head):

	ptr = head

	if head == None or head.next == None:
		return
	
	c = 0
	while ptr!= None and c< k:
		ptr = ptr.next
		c = c+1

	temp = ptr

	while temp.next!= None:
		temp = temp.next

	temp.next = head
	head = ptr.next
	ptr.next = None


