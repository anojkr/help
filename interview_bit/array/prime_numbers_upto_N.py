import math
def solve(N):
	H = N*N
	L = int(math.sqrt(H))

	M = [1 for i in range(0, H)]
	M[0] = 0
	M[1] = 0

	for i in range(2, L):
		if M[i] == 1:
			j = 2
			while (i*j < H):
				M[i*j] = 0
				j+=1
	
	r = []
	for i in range(H):
		if M[i] == 1:
			r.append(i)
	print(len(r))
	print(r)


if __name__ == '__main__':
	solve(10)