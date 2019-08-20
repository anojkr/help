class Product:

	count = 0

	def __init__(self, pid, types):
		print("-----Product is added------")
		self.pid = pid
		self.types = types
		Product.count += 1

class TV:

	tv_count = 0

	def __init__(self, pid, types, brand, cost):
		Product.__init__(self, pid, types)
		print("-----Mobile is added to stock------")
		self.brand = brand
		self.cost = cost
		TV.tv_count +=1

	def get_details(self):
		print('\n')
		print("----Tv Details----")
		print('Product Id	:	'+str(self.pid))
		print('Product type 	:	'+str(self.types))
		print('TV brand 	:	'+str(self.brand))
		print('TV cost		:	'+str(self.cost))
		print('Product count 	:	'+str(Product.count))
		print('TV  count 	: 	'+str(self.tv_count))


class Mobile:

	mobile_count = 0

	def __init__(self, pid, types, brand, cost):
		Product.__init__(self, pid, types)
		print("-----Mobile is added to stock------")
		self.brand = brand
		self.cost = cost
		Mobile.mobile_count +=1

	def get_details(self):
		print('\n')
		print("----Mobile Details----")
		print('Product Id	:	'+str(self.pid))
		print('Product type 	:	'+str(self.types))
		print('Mobile brand 	:	'+str(self.brand))
		print('Mobile cost	:	'+str(self.cost))
		print('Product count 	:	'+str(Product.count))
		print('Mobile  count 	: 	'+str(self.mobile_count))


p1 = Mobile(101, 'mobile' ,'samsung', 10000)
p2 = TV(102, 'TV' ,'Onida', 50000)
p1.get_details()
p2.get_details()