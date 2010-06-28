from FunctionTask import FunctionTask
from pack.pack1 import abc
import bar.foo
import math

k = 4

class fun():

	def foo2(self,x):
		print self.foo3(x)
	
	def foo3(self,y):
		return 2 * y	

def foo(m ,n = 10):
	print foo1(m, n)

def foo1(x,y):
#	return bar.foo.add(x , y)
#	return abc.mul(x,y)
#	return math.pow(x,y)
	return x*y

f = fun()

l = locals().copy()
g = globals().copy()	

F = FunctionTask([l,g], globals())



#Creating the Environment
#del globals()['foo1']
del globals()['k']
del globals()['abc']
del globals()['bar']
del globals()['math']


F.serialize(foo,(foo1,2))	
