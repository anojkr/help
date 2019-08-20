
# https://www.geeksforgeeks.org/minimum-number-of-towers-required-such-that-every-house-is-in-the-range-of-at-least-one-tower/
# Complexity O(N)

import sys

def tower(arr, r):
	N = len(arr)
	l = []

	arr.sort()
	tower = 0
	i = 0

	while (i < N):
		tower+=1
		loc = arr[i] + r
		while (i < N  and arr[i] <= loc):
			i = i +1
		i = i - 1
		
		loc = arr[i] + r
		print(arr[i])

		while (i < N  and arr[i] <= loc):
			i = i +1


	print(tower)

if __name__ == '__main__':
	arr = [ 7, 2, 4, 6, 5, 9, 12, 11 ]
	# arr = [1,5,15,20]
	r = 2
	tower(arr, r)
