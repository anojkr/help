import sys
import copy
from collections import defaultdict

def longest_substring_with_k_charater(s, m):
	st = list(s)
	n = len(st)

	hash_s = defaultdict()
	w = 0
	start = 0
	for i in range(0, n):
		if st[i] not in hash_s and w <= m:
			hash_s[st[i]] = 1
			w +=1
		elif st[i] in hash_s and w<=m:
			hash_s[st[i]] += 1 
		elif w > m:
			while len(set(st[start:i+1])) > m:
				hash_s[st[start]] -= 1
				start = start + 1
				w -= 1

	print(st[start:i+1])


if __name__ == '__main__':
	s = "aabacbebebe"
	m = 3
	longest_substring_with_k_charater(s, m)