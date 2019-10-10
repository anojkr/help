# cook your dish here
# A = [(1, 100, 10), (2,99, 11), (3, 98, 12), (4, 97, 8), (5, 96, 9)]
# p = sorted(A, key = lambda x : x[0])
# print(p)

d = {
    '5' : [(10, 100), (15, 95), (5, 90)],
    '6' : [(1, 2), (0, 3),(7, -1)],
    '1' : [(9,0), (-1, 2),(10, -3)]
}


p = sorted(d.items())

for k, val in d.items():
    # print(k, val)
    val.sort(key = lambda x:x[1])
    
print(d)