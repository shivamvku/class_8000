import mod1

# print(dir(mod1))


from mod1 import add
from mod1 import *
print(mod1.__doc__)

print(mod1.add.__doc__)

add(5,67)
sub(56,2)