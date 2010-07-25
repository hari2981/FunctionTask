from pydra.cluster.tasks.function.FunctionClient import FunctionClient
import math


def foo(m ,n = 10):
	return m * n

def foo1(x,y):
	return x * y


F = FunctionClient()
a = 5	
F.run(foo,(a,), n = 3)
print F.result()	
