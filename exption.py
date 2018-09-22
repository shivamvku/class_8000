# Excption handling

# Hnadling the inbult Excption
# Use deine Excption

# inbult Excption
# ===========================

# a = 1
# b = 0

# print(a/b)

# Handling the exptions

# try , except


# try -------------> you write the actual code
# whic you want execute

# except -------< you write the handing of exptions raised from the try block


# Single Excption handing
# ============================
# try:
# 	a = int(input('Enter a number --1\n'))

# 	b = int(input('Enter a number --2\n'))

# 	print(a/b)
# except ZeroDivisionError:
# 	print('Ther eis zero in denominator\n')


# Multpile Excption handing
# =================================
# try:
# 	a = int(input('Enter a number --1\n'))

# 	b = int(input('Enter a number --2\n'))

# 	print(a/b)
# except ValueError:
# 	print('Chek your input\n')
# except ZeroDivisionError:
# 	print('Ther eis zero in denominator\n')


# try:
# 	a = int(input('Enter a number --1\n'))
# 	b = int(input('Enter a number --2\n'))
# 	print(a/b)
# except (ZeroDivisionError,ValueError):
# 	print('Check your inputs\n')

# a = int(input('Enter a number --1\n'))
# b = int(input('Enter a number --2\n'))

# if a%b == 0:
# 	print('even')


# else -----> it get executed when there is no excption raised

# finally  ---- > it alwasys get executed

try:
	a = int(input('Enter a number --1\n'))
	b = int(input('Enter a number --2\n'))
	print(a/b)
except (ZeroDivisionError,ValueError):
	print('Check your inputs\n')
else:
	print('The result is ',a/b)
finally:
	print('The program ended\n')

















