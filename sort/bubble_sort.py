import sys

def bubble_sort(arr, N):
	for i in range(0, N):
		flag = 0
		for j in range(0, N-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				flag = 1
		if flag == 0:
			break

if __name__ == '__main__':
	arr = [1,2,3,5,4,6,7,8]
	N = len(arr)
	print(arr)
	bubble_sort(arr, N)
	print(arr)