
def add_number_list(head1, head2)

	ptr1 = head1
	ptr2 = head2

	if ptr1 == None:
		return ptr2

	if ptr2 == None:
		return ptr1

	carry = 0
	res = None
	prev = None

	while ptr1 != None or ptr2 != None:

		X = 0 if ptr1 == None else ptr1.data
		Y = 0 if ptr2 == None else ptr2.data
		Z = X + Y + carry

		S = Z/10
		carry = Z%10

		temp = Node(S)

		if res == None:
			res = temp

		else:
			prev.next = temp

		prev = temp

		if ptr1.next != None:
			ptr1 = ptr1.next

		if ptr2.next != None:
			ptr2 = ptr2.next

	if carry > 0:
		prev.next = Node(carry)

	return res



