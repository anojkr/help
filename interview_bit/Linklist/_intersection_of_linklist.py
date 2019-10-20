
def solve(ptr1, ptr2, k):
	
	c = 0

	if ptr1 == None or ptr2 == None:
		return None

	while ptr1!= None and c < k
			ptr1 = ptr1.next
			c = c+1
	
	while ptr1!= None and ptr2!= None:
		
		if ptr1 == ptr2:
			return ptr1

		ptr1 = ptr1.next
		ptr2 = ptr2.next

	return -1

def intersection(r, t):
	ptr1 = r
	ptr2 = t

	c1 = get_size(r)
	c2 = get_size(t)


	if c1 >= c2:
		d = c1-c2
		return solve(ptr1, ptr2, d)

	elif c1 < c2:
		d = c2-c1
		return solve(ptr2, ptr1)

