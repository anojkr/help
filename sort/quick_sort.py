import sys

def partition(arr, low, high):
	N = high-low+1
	q = arr[high]

	j = low-1
	for i in range(low, high+1):
		if arr[i] <= q:
			arr[i], arr[j] = arr[j], arr[i]
			j=j+1
	arr[i], arr[j] = arr[j], arr[i]
	return j+1

def quick_sort(arr, low, high):
	if low < high:
		p = partition(arr, low, high)
		quick_sort(arr, low, p-1)
		quick_sort(arr, p+1, high)

if __name__ == '__main__':

	arr = [9,9,8,8,7,7,3,3,1]
	n = len(arr)
	print(arr)
	quick_sort(arr, 0, n-1)
	print(arr)