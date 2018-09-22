class Avngers():
	# self ----------> conventional way

	def __init__(self,fn,ln,pay):
		# self.var = value
		self.fn = fn
		self.ln = ln
		self.pay = pay
	def fname(self):
		# print('In the method',self)
		print("name is :",self.fn)
	def lname(self):
		print('Last name is:',self.ln)
	def payment(self):
		print('payment is :',self.pay)


# Avngers.fname('Batman')
# Avngers.lname('Avngers')
# Avngers.payment(45000)

# Avngers.fname('superman')
# Avngers.lname('Avngers')
# Avngers.payment(50000)

# Avngers.fname('Ironman')
# Avngers.lname('Avngers')
# Avngers.payment(560000)

avg1 = Avngers('Batman','Avngers',5634434)
avg2 = Avngers('superman','reddy',987756)
# print('The avg1',avg1)
# print(Avngers())
avg1.fname()
avg1.lname()
avg1.payment()

avg2.fname()
avg2.lname()
avg2.payment()

