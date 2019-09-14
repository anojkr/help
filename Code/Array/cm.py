from collections import defaultdict
a = ['d', 'c','c','b','b','b','a','a','a','a']
d = {}
for i in a:
	if i not in d:
		d[i] =  1
	else:
		d[i] += 1

k = sorted(d.items(), key= lambda x: x[0], reverse = True)
print(d)
print(k)
