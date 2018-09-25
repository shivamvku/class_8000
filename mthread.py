





import os
from os import *

import threading
from threading import *







# Thread
# (self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None)



def suq(a):
	print('The name of the thread is ',threading.current_thread().name)
	print('The process id of', threading.current_thread().name,'is',os.getpid())
	print('The output is of', threading.current_thread().name,'is',a**2)

def cube(a):
	print('The name of the thread is ',threading.current_thread().name)
	print('The process id of', threading.current_thread().name,'is',os.getpid())
	print('The output is of', threading.current_thread().name,'is',a**3)



if __name__ == '__main__':
	print('The name of the thread is ',threading.current_thread().name)
	print('The Process id if the main fun is {}'.format(os.getpid()))

	t1 = threading.Thread(target = suq,name = 'square thread',args = (2,))
	t2 = threading.Thread(target = cube,name = 'Cube thread',args = (2,))

	t1.start()
	print(t1.is_alive())
	t2.start()
	t1.join()
	t2.join()
	
	print(t1.is_alive())