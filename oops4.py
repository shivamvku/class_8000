# Method Overring
# =======================


# class Animal():
# 	def __init__(self,name):
# 		self.name = name
# 	def eating(self):
# 		print(self.name,'animal is eating')
# 	def sleep(self):
# 		print(self.name,'is sleeping')

# class Loin(Animal):
# 	def eating(self):
# 		print(self.name,'is eating')
# 	def hunt(self):
# 		print(self.name,'is hunting')


# A1 = Animal('LOIN')
# A1.eating()


# L1 = Loin('leo')
# L1.eating()


# super() ---------- >  inbuilt fuction

# Achive a databstraion u use super fuction

# -------------------------
# simple inhertance
# ---------------------

# class Animal():

# 	def __init__(self,name1):
# 		self.name1 = name1
# 		print(self.name1,'is an animal')

# 	def eating(self):
# 		print(self.name1,'is eating')
# 	def sleep(self):
# 		print(self.name1,'is sleeping')

# class Loin(Animal):
	
# 	def __init__(self,name2):
# 		self.name2 =name2
# 		super().__init__('Sheru')
# 		print('This is very dangerous Animal')

# 	def roar(self):
# 		print(self.name2,'is roaring')
# 	def hunt(self):
# 		print(self.name2,'is hunting')



# l1 = Loin('Leo')
# l1.roar()
# l1.eating()






class Animal():
	def __init__(self,name1):
		self.name1 = name1
	def eating(self):
		print(self.name1,'is eating')
	def sleep(self):
		print(self.name1,'is sleeping')

class Loin(Animal):
	def __init__(self,name2):
		self.name2 = name2
	def roar(self):
		print(self.name2,'is roaring')
	def hunt(self):
		print(self.name2,'is hunting')

class Tiger(Loin):
	def __init__(self,name3):
		self.name3 = name3
		# super(Loin,self).__init__()
	def run(self):
		print(self.name3,'is Running')
	def swiming(self):
		print(self.name3,'is swiming')

class Aqua(Tiger):
	def __init__(self,name2,name3,name1,name4):
		
		super().__init__(name1)
		super(Loin,self).__init__(name2)
		super(Tiger,self).__init__(name3)
		self.name4 = name4
		print(self.name4)
		print(self.name3)
		print(self.name2)
		print(self.name1)

	def roam(self):
		print(self.name4,'is Roaming')
	def play(self):
		print(self.name4,'is Playing')



a1 = Aqua('name1','name2','name3','name4')

# a1.roam()

# a1.run()

# a1.roar()

# a1.sleep()