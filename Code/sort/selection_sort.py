# https://www.youtube.com/watch?v=GUDLRan2DWM

import sys

def selection_sort(arr, N):
	for i in range(0, N):
		min_x = i
		for j in range(i+1, N):
			if arr[min_x] > arr[j]:
				min_x = j
		arr[i], arr[min_x] = arr[min_x], arr[i]

if __name__ == '__main__':
	arr = [9,9,8,8,1,1,4,4,2,2,3,3]
	# arr = [1,2,4,5,6,7]
	N = len(arr)
	print(arr)
	selection_sort(arr, N)
	print(arr)