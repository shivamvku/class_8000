
# Function defination
# ----------------------------
# def greet():
# 	print('Hello wecome to digitalLync\n')
# 	# a =1
# 	# b =2

# # function call
# # ----------------_

# # function call is done by calling the function nname

# print(greet)
# greet()

# Arguments
# -----------------

# def functoinname(Arguments):
# 	function body
# 	.............
# 	............
# 	..............
# 	................
# 	..............
# functoinname(parameters)


# 1.postional Arguments
# 2.Default Arguments
# 3.keyword Arguments
# 4.Arbitarty or varibale length Arguments


# 1.postional Arguments
# ----------------------------------------
# a = 1
# b = 2
# def add():
# 	print(a+b)

# add()

# def add(a,b):
# 	print(a+b)

# x = int(input('Enter a number\n'))
# y = int(input('Enter a number\n'))
# add(x,y)

# def fibo(n):
# 	a = 0
# 	b = 1
# 	while a<n:
# 		print(a,end=' ')
# 		a,b = b,a+b
# 	print()
# y = int(input('Enter a number\n'))

# fibo(y)

# 0 1 1 2 3 5 8 13 21 34 55 89 144.................




# Default Arguments
# --------------------------
def add(a=1,b = 2):
	print(a+b)
add()


def add(a=1,b = 2):
	print(a+b)
add(10,45)
