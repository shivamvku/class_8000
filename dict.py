# d = {'hi':45,1:'apple',56.234:'mango',56.234:[1,2,3,4],56.234:'Nokia'}
# print(d[56.234])

# print(d['hi'])
# print(d)
# # d['hi'] = 'somtinh'
# # del d['hi']
# d2 = {1:'Apple',2:'Nokia',3:'Samusng',4:'somthing'}
# # print(d2)
# # d2.popitem()
# # d2.pop(3)
# print(d2.keys())
# print(d2.values())
# print(d2.items())
# print(d2)

# t = (1,2,3,['mango','apple'],45,22,34)
# l = [56,34,66,9900,('Samusng','Nokia'),445.23]

# print(t[3][1])
# print(l[4][1])
# print(t)
# t[3][1] = 'pineapple'

# print(t)
# print(l)
# l[4][1] = 'chinamobile'
# print(l)



# dict comprehesnion
d = {a:a**2 for a in range(0,11)}
# print(d)

# .formkeys(keys,squ)

# keys = ['apple','superman','batman','ironman']
# val  =  ['fruit','avnger1','avnger2','avnger3']
# d = dict.fromkeys(keys,val)
# print(d)


print(len(d))
print(all(d))
print(any(d))
print(sum(d))
print(min(d))
print(max(d))