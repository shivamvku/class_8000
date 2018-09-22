# ======================
# Simple inhertance
# ======================

# class Animal():
# 	def __init__(self,name):
# 		self.name = name
# 	def eating(self):
# 		print(self.name,'is eating')
# 	def sleep(self):
# 		print(self.name,'is sleeping')

# class Loin(Animal):
# 	def roar(self):
# 		print(self.name,'is roaring')
# 	def hunt(self):
# l1 = Loin('Sheru')
# l1.roar()
# l1.hunt()
# l1.eating()
# l1.sleep()

# l2 = Loin('leo')
# l2.roar()
# l2.hunt()
# l2.eating()
# l2.sleep()


# ==============================
# Multiple Inhertance
# ==============================

# Type - 1
# ------------


# class Animal():
# 	def __init__(self,name):
# 		self.name = name
# 	def eating(self):
# 		print(self.name,'is eating')
# 	def sleep(self):
# 		print(self.name,'is sleeping')

# class Loin(Animal):
# 	def roar(self):
# 		print(self.name,'is roaring')
# 	def hunt(self):
# 		print(self.name,'is hunting')

# class Tiger(Animal):
# 	def run(self):
# 		print(self.name,'is Running')
# 	def swiming(self):
# 		print(self.name,'is swiming')

# class Aqua(Animal):
# 	def roam(self):
# 		print(self.name,'is Roaming')
# 	def play(self):
# 		print(self.name,'is Playing')

	
# fsh1 = Aqua('nemo')
# fsh1.eating()
# fsh1.sleep()
# fsh1.roam()
# fsh1.play()

# l1 = Loin('Sheru')
# l1.roar()
# l1.hunt()
# l1.eating()
# l1.sleep()


# t1 = Tiger('vijay')
# t1.run()
# t1.swiming()
# t1.eating()
# t1.sleep()



# Type ------ 2
# ---------------------

class Animal():
	def __init__(self,name):
		self.name = name
	def eating(self):
		print(self.name,'is eating')
	def sleep(self):
		print(self.name,'is sleeping')

class Loin():
	def __init__(self,name):
		self.name = name
	def roar(self):
		print(self.name,'is roaring')
	def hunt(self):
		print(self.name,'is hunting')

class Tiger():
	def run(self):
		print(self.name,'is Running')
	def swiming(self):
		print(self.name,'is swiming')

class Aqua(Animal,Tiger,Loin):
	def roam(self):
		print(self.name,'is Roaming')
	def play(self):
		print(self.name,'is Playing')


	
fsh1 = Aqua('nemo')
fsh1.eating()
fsh1.sleep()
fsh1.roam()
fsh1.play()
fsh1.swiming()
# fsh1.roar()
# fsh1.hunt()
# fsh1.run()






# ===============================
# Mult-level Inhertance
# ================================


class Animal():
	def __init__(self,name):
		self.name = name
	def eating(self):
		print(self.name,'is eating')
	def sleep(self):
		print(self.name,'is sleeping')

class Loin(Animal):
	def roar(self):
		print(self.name,'is roaring')
	def hunt(self):
		print(self.name,'is hunting')

class Tiger(Loin):
	def run(self):
		print(self.name,'is Running')
	def swiming(self):
		print(self.name,'is swiming')

class Aqua(Tiger):
	def roam(self):
		print(self.name,'is Roaming')
	def play(self):
		print(self.name,'is Playing')


print(60*'=')
print('Prporties of Aqua Animal\n')
fsh1 = Aqua('nemo')
fsh1.eating()
fsh1.sleep()
fsh1.roam()
fsh1.play()
fsh1.swiming()
fsh1.roar()
fsh1.hunt()
fsh1.run()
print(60*'=')
print('Prporties of Carnivors\n')
t1 = Tiger('vijay')
t1.run()
t1.swiming()
t1.roar()
t1.hunt()
t1.eating()
t1.sleep()
print(60*'=')
print('Prporties  of Loin\n')
l1 = Loin('Sheru')
l1.roar()
l1.hunt()
l1.eating()
l1.sleep()




















