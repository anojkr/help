class A:

	def __init__(self):
		pass

	def area(self, l):
		print('Area of cube:' + str(int(l)*int(l)*int(l)))

	def area(self, l, b):
		print('Area of triangle:' + str(0.5*int(l)*int(b)))

	def area(self, l, b, h):
		print('Area of rectangle:' + str(int(l)*int(b)*int(h)))



p1 = A()
p1.area(2)
p1.area(2,4)
p1.area(2,4,5)

