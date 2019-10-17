# https://www.youtube.com/watch?v=i-SKeOcBwko

import sys

def insertion_sort(arr, N):
	for i in  range(0, N):
		temp = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > temp:
			arr[j+1] = arr[j] 
			j = j - 1
		arr[j+1] = temp

if __name__ == '__main__':
	arr = [9,9,8,8,7,7,3,3,1]
	N = len(arr)
	print(arr)
	insertion_sort(arr, N)
	print(arr)