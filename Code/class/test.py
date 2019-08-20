import sys
import time

class Employee:
	
	raise_amount = 2.0
	emp_cnt = 0
	dept = 'HR'

	def __init__(self, eid, name, sex, age, salary):
		self.eid = eid
		self.name = name
		self.sex = sex
		self.age = age
		self.salary = salary
		Employee.emp_cnt +=1

	def get_emp_details(self):
		print('\n')
		print('--------Employee ID: ' +str(self.eid) + '----------')
		print('Name 	: ' + str(self.name))
		print('Sex  	: ' + str(self.sex))
		print('Age  	: ' + str(self.age))
		print('Salary  : ' + str(self.salary))
		print('Dept  	: ' + str(self.dept))

	@classmethod
	def no_of_employee(cls):
		print('No. of employee: ' + str(cls.emp_cnt)) 

	@staticmethod
	def time():
		print(str(time.time()))

	def change_department(self, dept):
		self.dept = dept

	@classmethod
	def change_department_all(cls):
		cls.dept = 'Production'

e1 = Employee('2018065','Anoj', 'Male', '25', 10000)
e2 = Employee('2018067','Ravi', 'Male', '24', 20000)

e1.get_emp_details()
e2.get_emp_details()
e1.change_department('Finance')
Employee.change_department_all()
e1.get_emp_details()
e2.get_emp_details()

