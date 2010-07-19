from FunctionTask import FunctionTask
import unittest
import math	

class fun():
    def double(self,x):
        return x * 2	    

def my_pow(x, y):
    return math.pow(x,y)	

def foo(x, y = 10):
    return mul(x,y)

def my_exec(f, x):
    return f(x) 	

def mul(x, y):
    return x * y	


class cases(unittest.TestCase):
	
    def setUp(self):
	self.l = locals().copy()
        self.g = globals().copy()	
        self.F = FunctionTask([self.l,self.g],globals()) 

    def test_initial(self):
	"""Testing Function dependency """ 
	del globals()['mul']
	self.F.serialize(foo,(2,))

    def test_arguments_type(self):
	""" Arguments should be specified in tuples """    
	self.assertRaises(TypeError,self.F.serialize,(foo,[2,]))
    
    def test_argument(self):
        """ Testing type of argument in Arguments """
        f = fun()
        self.assertRaises(TypeError,self.F.serialize,(my_exec,(f.double,3)))	    
	    
    def test_function(self):
	"""function type should not be class instance method """ 
	f = fun()   
	self.assertRaises(TypeError,self.F.serialize,(f.double,(2,)))
    
    def test_modules(self):
 	"""Testing Module dependency"""	   
	del globals()['math']
	self.F.serialize(my_pow,(2,3))
	    
	     
    def tearDown(self):
	del self.l	
	del self.g	
	del self.F	


if __name__ == "__main__":
    unittest.main()
