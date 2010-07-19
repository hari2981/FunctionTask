import cPickle as pickle
import types

#Define exceptions
class FunctionTaskError(Exception):pass


class FunctionTask():

    def __init__(self, globals_list):
        self.__pickle_proto = 0
	self.__modules = []
	self.__objects = {}
	self.__globals_list = globals_list

    def serialize(self, func, args, **kwargs):  

	if not isinstance(func,types.FunctionType):
	    raise TypeError("\nfunc should be FunctionType")

	if not isinstance(args, tuple):
    	    raise TypeError("\nArguments must specified in  tuple")
        
	for arg in args:
	    if isinstance(arg, types.MethodType) and \
	    	isinstance(arg, types.InstanceType) :
                raise TypeError("\nArguments should not be instance type")

        self.__find_objects(func, args, **kwargs)	
#	print "Dependent objects %s" % self.__objects 

	serialized = pickle.dumps((func, args, kwargs, self.__objects),
			self.__pickle_proto)	
	return serialized

    def work(self,serialized):
	func, args, kwargs , objects = pickle.loads(serialized)
        func(*args, **kwargs) 	

		

    def __find_objects(self,func, args,**kwargs):
	"""Create a dict by extracting from globals and locals
	
	"""
    	while 1:                                                        
            try :                                                      
   	        func(*args, **kwargs)                                       
	   	break                                                  
	    except NameError as error:
           	name =  error.args[0].split('\'')[1::2][0]
		object = self.get_item(name)
	        self.__global_ref.__setitem__(name,object)


    def get_item(self, name):
	for dict in self.__globals_list:
	    for key, item in dict.items():

		if name == key:

		    if not isinstance(item,types.ModuleType): 
	            	self.__objects.__setitem__(name,item)
		    else :
		        index = item.__name__.rfind('.')

			if index != -1:
			    self.__objects.__setitem__(name,item.__name__[:index])
			else :
			    self.__objects.__setitem__(name,item.__name__)	

	            return item	
		               
