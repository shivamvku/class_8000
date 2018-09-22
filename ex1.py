# l = [1,2,3,4,5,6,7,8,9,10]

# a = [[1,2],[3,4]]
# b = [[4,5],[6,7]]

# # sum=  [5,7,9,11]

# # a[0][0]+b[0][0] ==== 5
# # a[0][1]+b[0][1]====== 7
# # a[1][0]+b[1][0] ====== 9
# # a[1][1]+b[1][1] === 11
# c =[]

# for i in range(len(a)):
# 	for j in range(len(a[i])):
#  		s = (a[i][j]+b[i][j])
#  		c.append(s)
# print(c)

# a = (1,2,3,4)
# print(a.index(4))

# genrator objects
# packeing of tuple
# t = [a for a in range(0,11)]
# print(t)
# t = (a for a in range(0,11))
# print(t)

# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))

# for a in t:
# 	print(a)


# enumerator
# ==================
# enumerate()-------------- enumerator object it contais the tuple of  index nuber and value at that index

l = ['apple','Nokia','samsung']
enum = enumerate(l)
print(type(enumerate))
# print(enum)
# print(next(enum))
# for a in enum:
# 	print(a)
print([a for a in enum])