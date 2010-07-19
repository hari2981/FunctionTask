from FunctionClient import FunctionClient
import math


def foo(m ,n = 10):
	return m * n

def foo1(x,y):
	return x * y


l = locals().copy()
g = globals().copy()	

F = FunctionClient([l,g])
F.run(foo,(5,), n = 2)
print F.result()	
