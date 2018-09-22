


# defing a class in python

# syntax
# --------------
# class Clasname(objects):
	# body of the classs 



# class employe():
# 	''' This is an emptly employe class'''
# 	print('Hi i am employe class')
# 	a =34
# 	b = 45

# print(employe)
# print(employe())
# print(employe.a)
# print(employe.b)
# print(employe.__doc__)




# class employe():
# 	a = 10
# 	def name():
# 		print('hello i am from name function') 
# # print(employe.a)
# # print(employe.name())
# employe.name()




class Emp():
	def Fname(fname):
		print('The name of the person is :',fname)

	def Lname(lname):
		print('The last name of the person is:',lname)

	def Email(fname,lname):
		print('The email is {}.{}n@avngers.com'.format(fname,lname))


Emp.Fname('Batman')
Emp.Lname('Avnger')
Emp.Email('Batman','Avnger')
