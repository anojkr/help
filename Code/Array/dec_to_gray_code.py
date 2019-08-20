def grayCode(A):
	res = []
	for i in range(0, 2**A):
		b = bin(i)
		res.append('0'*(A-len(b[2:])) + b[2:])

	r = []
	for i in range(0, len(res)):
		temp = list(map(int, list(res[i])))
		gray = []
		gray.append(temp[0])
		for i in range(1, len(temp)):
			gray.append(temp[i-1]^temp[i])
		r.append("".join(map(str, gray)))
	result = []
	for i in range(0, len(r)):

		result.append(int(r[i], 2))
	print(result)
	return result



if __name__ == '__main__':
 	grayCode(4)