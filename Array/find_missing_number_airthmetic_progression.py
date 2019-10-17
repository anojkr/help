
def ap(a, d, i):
	return a + i*d

def binary_search(arr, N, low, high):
	a = arr[0]
	d = arr[1]-arr[0]
	if low <= high:
		mid = (low+high)//2
		if arr[mid]-arr[mid-1] != d:
			return ap(a, d, mid)
		if arr[mid] != ap(a, d, mid):
			return binary_search(arr, N, low, mid-1)
		else:
			return binary_search(arr, N, mid+1, high)






if __name__ == '__main__':
	arr =  [2,4,6,10,12,14]
	N 	= len(arr)
	print(binary_search(arr, N, 0, N-1))
