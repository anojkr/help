
def solve(head, n):
	
	ref_ptr = head
	main_ptr = head

	if head == None or head.next == None:
		return None

	c = 0
	while ref_ptr != None and c<n:
		ref_ptr = ref_ptr.next
		c = c + 1

	while  ref_ptr!= None:
		main_ptr = main_ptr.next
		ref_ptr = ref_ptr.next

	return main_ptr.data
