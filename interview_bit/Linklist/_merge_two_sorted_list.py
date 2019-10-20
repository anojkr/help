
def merge(r, t):
	ptr1 = r
	ptr2 = t

	if ptr1 == None:
		return ptr2

	if ptr2 == None:
		return ptr1

	temp = None
	
	if ptr1.data <= ptr2.data:
		temp = ptr1
		ptr1.next = merge(ptr1.next, ptr2)

	elif ptr1.data > ptr2.data:
		temp = ptr2	
		ptr2.next = merge(ptr1, ptr2.next)

	return temp
