from collections import defaultdict
a = ['b', 'b', 'a', 'a','c','c','c', 'd', 'd','d','d']
d = {}
for i in a:
	if i not in d:
		d[i] =  1
	else:
		d[i] += 1

k = sorted(d.items())
print(d)
print(k)
