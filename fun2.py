# oreder of passing Argumets

# postiona Argumets
# defaul Argumets
# arbitarty


# def add(b,a =1):
# 	print(a+b)
# add(5)


# keyword Argumets
# # ---------------------

# syntax
# -------

# def add(a,b):
# 	print(a+b)

# add(a=1,b =2) 

# arbitarty Argumets or variable length  Argumets
# -----------------------------------------------------
# Type -1
# ------------------
# def welc(*args):
	
# 	# print(type(a))
# 	for v in args:
# 		print('Welcome',v,'to python class\n')

# welc('Superman','Batman','Ironman','Avnegers','Hulck')

# # Type ----------2
# # ==================++

# def details(**kwargs):
# 	# print(info)
# 	for name,address in kwargs.items():
# 		print('Welcome, he is {} from {}'.format(name,address))
# details(Batman = 'usa',Ironman = 'India',wonderwomen = 'Bangloor')

# return
# --------------
# return what function is giving
# def a():
# 	a = 5
# 	b = 'Hello'
# 	return a
# a()
# print(a())

# global and local variable
# ==================================
# a = 1
# # global
# def f1():
# 	a  = 3
# 	# print(a)				#arshiya : 1,5,7,9
# def f2():
# 	global a					#bahrgavi :3,5,7,9
# 	a = 5					#kishor : 9,5,7,9
# 	return a 				#joti:3,9,7,9
# def f3():
# 	global a 
# 	a = 7				
# 	return a
# print(a)
# f3()
# f1()
# f2()
# print(a)



# Lambda function or anaonmys function
# --------------------------------------


# lambda --- one line function

# syntax
# ------------

# function defination
# # ----------------------------
# lambda arg:body or expression

# # function call
# # -------------

# var = lambda arg:bodyo or expression

# var(parmetrs)
# def squ(a):
# 	return a**2
# print('This noraml function',squ(3))

# squ = lambda a : 'a**2'
# print('This is lambda function',squ(3))

# map() ------------>  map(func, *iterables) --> map object
# Make an iterator that computes the function
# using arguments from
# each of the iterables.  Stops when the shortest
# iterable is exhausted.

l = [a for a in range(1,21)]
print(l)

even = list(map(lambda a : a%2 == 0,l))
print(even)

# filter()

odd = list(filter(lambda a : a%2!=0,l))
print(odd)











