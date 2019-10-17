# https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

def solve(arr, N):
	hash_m   = {}
	max_len  = 0
	curr_sum = 0
	for i in range(N):
		if arr[i] == 0 and max_len == 0:
			max_len = 1
		curr_sum = curr_sum + arr[i]

		if curr_sum not in hash_m:
			hash_m[curr_sum] = i

		elif curr_sum in hash_m:
			max_len = max(max_len, i - hash_m[curr_sum])
	print(max_len)

	print(hash_m)
if __name__ == '__main__':
	arr =  [15, -2, 2, -8, 1, 7, 10, 23]
	N = len(arr)
	solve(arr, N)
