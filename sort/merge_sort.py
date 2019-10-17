import sys

def merge(arr, low, mid, high):
	n1 = mid - low + 1
	n2 = high - mid

	L = [0]*(n1+1)
	R = [0]*(n2+1)
	L[n1] = sys.maxsize
	R[n2] = sys.maxsize

	for i in range(0, n1):
		L[i] = arr[i+low]

	for j in range(0, n2):
		R[j] = arr[j+mid+1]
		
	i = 0
	j = 0
	for k in range(0, n1+n2):
		if L[i] < R[j] and i < n1:
			arr[low+k] = L[i]
			i += 1
		elif L[i] >= R[j] and j < n2:
			arr[low+k] = R[j]
			j += 1


def merge_sort(arr, low, high):
	if low < high:
		mid = (low + high)//2
		merge_sort(arr, low, mid)
		merge_sort(arr, mid+1, high)
		merge(arr, low, mid, high)

if __name__ == '__main__':
	arr = [9,9,8,8,7,7,3,3,1]
	n = len(arr)
	print(arr)
	merge_sort(arr, 0, n-1)
	print(arr)