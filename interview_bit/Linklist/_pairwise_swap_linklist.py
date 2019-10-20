
def swap(ptr1, ptr2);
	ptr1.data, ptr2.data = ptr2.data, ptr1.data


def pair_swap(head):

	ptr = head
	if head == None or head.next == None:
		return None

	while ptr!= None:
		swap(ptr, ptr.next)
		ptr = ptr.next.next











