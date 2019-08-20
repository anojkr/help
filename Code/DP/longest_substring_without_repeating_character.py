import sys
import copy

def longest_substring_without_repeating_character(s):
	st = list(s)
	n = len(st)
	m = 0
	s_set = set()
	start = 0
	end = 0
	for i in range(0, n):
		if st[i] not in s_set:
			s_set.add(st[i])
		else:
			while (start < i):
				if (st[start] == st[i]):
					start = start + 1
					break
				s_set.remove(st[start])
				start = start + 1

		m  = max(m, i-start + 1)
	print(m)

if __name__ == '__main__':
	s = "ABDEFGABEF"
	longest_substring_without_repeating_character(s)