# Sets
# ------------------

# a = {1,2,3,4,5,6}
# b = {}

# print(a)
# print(b)
# print(type(a))
# print(type(b))


# set() ------- > empty set and set function
# data typles suppoorted for set
# int , float, str , tuple/list , complex 



# b = {1,'ironman',56.33,6+9j}
# # print(b[1])
# print(b)
# # b.add(45)
# # b.update({3,22})
# # b.update([3,22,55,334,22])
# # b.pop()
# # b.remove(1)
# # b.discard(56.33)
# print(b)


#
# {}

a = {1,2,3,4,5}
b = {6,5,3,7,8}

# Union
# # ___________

print(a|b)
print(a.union(b))

# interstin
# ______________


# print(a&b)
# print(a.intersection(b))

# issubset()
# issuperset()


# print(a-b)
# print(b-a)

# print(a.difference(b))

# print(b.difference(a))

# print(a.symmetric_difference(b))
# print(b.symmetric_difference(a))

# frozenset()
# -------------------


a = {1,2,3,4,5}
b = [56,34,2]
c= (45,22,34)
fz1 = frozenset(a)

fz2 = frozenset(b)

fz3 = frozenset(c)
print(fz1)
print(fz2)
print(fz3)

print(type(fz1))

print(type(fz2))


print(type(fz3))













