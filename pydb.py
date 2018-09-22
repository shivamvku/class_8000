
# Data Base
# =====================


# It is plae store your information(data)

	
	# Data
	# 	1.structure Data
	# 	2. Unstructure Data


	# structure data
	# --------------------			------------------
	# sequential Data 				Non sequential data
	# ---------------					---------------------
	# 	table						(NO-SQL)
	# 	row and coloum					xml
	# 									JASON format
	# (MySQl,SQl,SQlite3
	# ,oracladb,Prostgress SQl..)			(MongoDB)

	# Unstructure Data
	# -----------------------
		# textfile,mp3,video......
		# Bigdata (Ex:.hive....)

# To mange all the data we need a manger (DBMS)
	
# 	DBMS ---- > data base mangemnet system


# Queries
# =========
# ----> it is coomond given to the DBMS

# Operations
# # ============
# CRUD
# (Create , Read ,Update, Delete)




# ================================================

# Create database (python_8000)


# import pymysql

# #database connection
# connection = pymysql.connect(host="localhost",user="root",passwd="vineet@mysql",database="python_8000" )
# cursor = connection.cursor()
# # some other statements  with the help of cursor
# connection.close()


# Creating Table
# ------------------------

# import pymysql

# #database connection
# connection = pymysql.connect(host="localhost",user="root",passwd="vineet@mysql",database="python_8000" )
# cursor = connection.cursor()
# cursor.execute('''CREATE TABLE py800(id int,fname varchar(20),lname varchar(20),age int(200)) ''')
# # some other statements  with the help of cursor
# connection.close()




# INSERT DATA INTO DATABASE
# # ================================
# import pymysql

# #database connection
# connection = pymysql.connect(host="localhost",user="root",passwd="vineet@mysql",database="python_8000" )
# cursor = connection.cursor()
# cursor.execute(''' INSERT INTO py800(id,fname,lname,age) VALUES(1,'Batman','Avenger',40)''')
# cursor.execute(''' INSERT INTO py800(id,fname,lname,age) VALUES(2,'Superman','Avenger',46)''')
# # some other statements  with the help of cursor
# connection.commit()
# connection.close()





# # Data view
# # ============================

import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="vineet@mysql",database="python_8000" )
cursor = connection.cursor()
cursor.execute('''SELECT * FROM py800 ''')
data = cursor.fetchall()
# print(data)
for a in data:
	print(a)
# some other statements  with the help of cursor
connection.close()

