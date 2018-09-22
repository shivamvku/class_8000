# # CSV Files:
# # ===================
# # operations
# # # =----------
# # write --------- (data)
# # read file ----- (file)

#  reader(...)
#         csv_reader = reader(iterable [, dialect='excel']
#                                 [optional keyword args])
#             for row in csv_reader:
#                 process(row)
#  writer(...)
#         csv_writer = csv.writer(fileobj [, dialect='excel']
#                                     [optional keyword args])
#             for row in sequence:
#                 csv_writer.writerow(row)


# import csv
# def pen(fileobj,data):
# 	rd = csv.writer(fileobj,delimiter = ',')
# 	print(rd)
# 	print(data)

# 	for a in data:
# 		rd.writerow(a)

# def read(fileobj):
# 	rd = csv.reader(fileobj,delimiter=',')
# 	for a in rd:
# 		print(a)

# def read(fileobj):
# 	rd = csv.DictReader(fileobj,delimiter=',')
# 	for a in rd:
# 		print(a)
# if __name__ == '__main__':

	# fileobj = open('sample.csv','w')
	# data = ['fname,lame,age,address'.split(','),
	# 		'Batman,avnger,40,usa'.split(','),
	# 		'supermna,avnger,40,usa'.split(','),
	# 		'ironman,avnger,40,usa'.split(','),
	# 		'wornderwomen,avnger,40,usa'.split(','),
	# 		'spiderman,avnger,40,usa'.split(','),
	# 		'himan,avnger,40,usa'.split(',')]

	# pen(fileobj,data)
	# fileobj = open('sample.csv','r')
	# read(fileobj)
	# fileobj.close()


# create a file:
# ========================
# encoding
# ----------------	
# by default --- utf -8
# open('filename.exexion','mode',encoding)

# fileobj = open('demo.txt','w')
# fileobj.write(''' # # CSV Files:
# # # ===================
# # # operations
# # # # =----------
# # # write --------- (data)
# # # read file ----- (file)

# #  reader(...)
# #         csv_reader = reader(iterable [, dialect='excel']
# #                                 [optional keyword args])
# #             for row in csv_reader:
# #                 process(row)
# #  writer(...)
# #         csv_writer = csv.writer(fileobj [, dialect='excel']
# #                                     [optional keyword args])
# #             for row in sequence:
# #                 csv_writer.writerow(row)


# # import csv
# # def pen(fileobj,data):
# # 	rd = csv.writer(fileobj,delimiter = ',')
# # 	print(rd)
# # 	print(data)

# # 	for a in data:
# # 		rd.writerow(a)

# # def read(fileobj):
# # 	rd = csv.reader(fileobj,delimiter=',')
# # 	for a in rd:
# # 		print(a)

# # def read(fileobj):
# # 	rd = csv.DictReader(fileobj,delimiter=',')
# # 	for a in rd:
# # 		print(a)
# # if __name__ == '__main__':

# 	# fileobj = open('sample.csv','w')
# 	# data = ['fname,lame,age,address'.split(','),
# 	# 		'Batman,avnger,40,usa'.split(','),
# 	# 		'supermna,avnger,40,usa'.split(','),
# 	# 		'ironman,avnger,40,usa'.split(','),
# 	# 		'wornderwomen,avnger,40,usa'.split(','),
# 	# 		'spiderman,avnger,40,usa'.split(','),
# 	# 		'himan,avnger,40,usa'.split(',')]

# 	# pen(fileobj,data)
# 	# fileobj = open('sample.csv','r')
# 	# read(fileobj)
# 	# fileobj.close()

#  ''')
# fileobj.close()

# cursor operations
# =======================
# chr ---- > 12,352
# offset ---> 
# 			0 --- row
# 			1 --- column
# seek(chr,offset) --------> move your cursor to desied position 
# tell(chr,offset) --------> give the curent position of cursor


fileobj = open('/home/vineet/Documents/vineet/python/class4_8000/candycrush/demo.txt','r')
# print(fileobj.read())
# print(fileobj.read(30)) #reading by char
# print(fileobj.readline(4))
# print(fileobj.readline(3))
# print(fileobj.readline(5))
# print(fileobj.readline(4))
# print(fileobj.readline(6))
print(fileobj.tell())
print(fileobj.read(30))
print(fileobj.tell())
print(fileobj.seek(0))
print(fileobj.read())
print(70*'-')
fileobj.seek(50)
print(fileobj.read())
print(fileobj.tell())
fileobj.seek(0,0)
print(fileobj.tell())
print(fileobj.read())

fileobj.close()