# # Data Hiding
# # ==================


# By in python 
# 	var
# 	methods are public
# in ored to any eethod or var private 

# 	var ------ >  public
# 	__var -----> private

# 	method1 -------> public
# 	__method1 ------> private

	# _var _method --------> protected



class Avengers():
	# payt = 100
	def __init__(self,fname):
		self.payment = 100
		# self.__hdpaymet = 5000  #Private varable
		self.fname = fname

	def pay(self):
		# print('The Payment of {} is {}'.format(self.fname,self.__hdpayment))
		print('The Payment of {} is {}'.format(self.fname,self.payment))
	
	def incpay(self,value):
		self.payment = self.payment + value
		# self.__hdpaymet = self.__hdpaymet+value


avg1 = Avengers('Batman')
avg1.pay()
avg1.incpay(1000)
avg1.pay()
print(avg1._Avengers__hdpaymet) #way to access the hiddin var 



