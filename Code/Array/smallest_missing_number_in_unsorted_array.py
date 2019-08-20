# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

def missing(res):
	N = len(res)
	
	for i in range(0, N):
		if res[i] < N and res[i] > 0:
			res[res[i]-1] = -res[res[i]-1]
	# print(res)
	for i in range(0, N):
		if res[i] > 0:
			return i+1



if __name__ == '__main__':
	arr = [1, 2, 3, 7, 6, 8, -1, -10, 15]
	res = []
	for item in arr:
		if item >= 0:
			res.append(item)
	print(res)
	print(missing(res))