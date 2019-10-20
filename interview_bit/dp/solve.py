


d = {
		"mobile" : 1,
		"samsung" : 1,
		"sam" : 1,
		"sung" : 1,
		"man" : 1,
		"mango" : 1,
		 "icecream" : 1,
		 "and" : 1,
		 "go" : 1,
		 "i" : 1,
		 "love" : 1,
		 "ice" : 1,
		 "cream" : 1
	}

result = ""
strm = "iloveicecreamandmango"
c = 0

def solve(s, dic, n):
	
	for i in range(0, n+1):
		global result 
		prefix = s[0:i]

		if prefix in dic:
			result = result + " "+ prefix
			global c
			c = c + i 
			if c == n+1:
				result = result + " "+ prefix
				print(result)
				return
			stm = s[i:]
			
			solve(stm, dic, n)





solve(strm, d, len(strm))