a = 'Digtial'
b = 'Lync'

# print(a[3])

# print(a[3:5])

# print(a[0::2])


# # str contaicnation
# print(a+b)
# print(5*a)
# print(a,b)

# inbult function in string
# ----------------------------------
a = 'asds'
b = 'Superman'

# print(len(a))
# print(min(a))
# print(max(a))
# print(ord(min(a)))
# print(ord(max(a)))
# print(type(a[3]))

# inbult methods in string

# print(a.upper())
# print(b.upper())
# print(b.lower())
# print(a.isalnum())
# print(a.isdecimal())
# print(b.center(2))
# d= 'Digitallync'
# print(d.istitle())

# ===================================

# string formating style

# Old formating style
# --------------------

a = 'batman'
b = 'Superan'

# type formater casters
# %s ============= str()
# %d --------------- int()
# %f ------------- float()
# print('%s and %s are the avengers'%(45,b))
# print('%d and %d are the marks of %s and %s avengers'%(45.3454325,90,a,b))

# print('%f and %f are the marks of %s and %s avengers'%(45.3454325,90.535465,a,b))


# New formating style fancier formating style
# ----------------------------------------------
# print('{0} and {1} are the marks of {2} and {3} avengers'.format(89.234565432,98.234533,a,b))

# print('{1} and {0} are the marks of {3} and {2} avengers'.format(89.234565432,98.234533,a,b))

# print('{:.2f} and {:.2f} are the marks of {:.2s} and {} avengers'.format(89.234565432,98.234533,a,b))



# Python String lstrip()	Removes Leading Characters
# Python String rstrip()	Removes Trailing Characters
# Python String strip()	Removes Both Leading and Trailing Characters
a = 'DigitalLync'

b = (20*'-'+a+20*'*')
print(b)
print(b.lstrip('-'))
print(b.rstrip('*'))
print(b.strip('*'))
print(b.strip('Digitallync'))