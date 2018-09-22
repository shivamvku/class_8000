
# Class methods and static methods
# ====================================
# static Method
# ---------------------

# Syntax
# ============================
# class a(obj):
# 	def dec_msg(anything):
# 		def inner_fun(content):
# 			return 'welcome to '+ anything(content)


# @staticmethod
# 	def method(ar1,arg2,arg3............)



# Static Methods
# =======================================
# Syntax
# -----------------------
# class sm(obj):
# 	@staticmethod
# 	def func(arg1,arg2,arg3.................):


# class Methods
# =============================
# Syntax
# ---------------
# class cm(objs):
# 	@classmethod
# 	def function(cls,arg1,arg2,arg3..............)

# # method-----> ths is function which can be used or get conveted into class method
#  what is return ?
#  	class method




# Example ------ 1
# ==========================
# check the age whther >18 or no is adult or not

import datetime
from datetime import *

class avngers():
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def dispdeatails(self):
		print('He is ',self.name,'of this',self.age,'age')

	@classmethod
	def fromdob(cls,name,year):
		return cls(name,date.today().year - year)

	@staticmethod
	def isadult(age):
		return age >= 18

avg1 = avngers('Superman',6)
avg2 = avngers.fromdob('Superman',2004)

print(avg2.age)
print(avg2.isadult(avg2.age))

avg2.dispdeatails()
avg1.dispdeatails()

