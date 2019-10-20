
def palindrome(head)

	if head == None or head.next == None:
		return 

	fast = head
	slow = head
	prev_slow = None

	while fast!= None and fast.next!= None:
		fast = fast.next.next
		prev_slow = slow
		slow = slow.next

	if fast != None:
		mid = slow
		slow = slow.next

	right = slow
	prev_slow.next = None

	right = reverse(right)
	res = compare(head, right)
	right = reverse(right)

	if mid != None:
		prev_slow.next = mid
		mid.nxt = right

	else:
		prev_slow.next = right

	return res


