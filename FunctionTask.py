import cPickle as pickle
import inspect
import types
from pydra.cluster.tasks import Task
import logging
logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)

#Define exceptions
class FunctionTaskError(Exception):pass


class FunctionTask(Task):

    def __init__(self):
        self.__pickle_proto = 0
	self.__modules = []
	self.__objects = {}
	Task.__init__(self,"FunctionTask")

    def serialize(self, func, args, **kwargs):  

	if not isinstance(func,types.FunctionType):
	    raise TypeError("\nfunc should be FunctionType")

	if not isinstance(args, tuple):
    	    raise TypeError("\nArguments must specified in  tuple")
        
	for arg in args:
	    if isinstance(arg, types.MethodType) and \
	    	isinstance(arg, types.InstanceType) :
                raise TypeError("\nArguments should not be instance type")

        serialized = self.__dump_funcs((func, ), args, **kwargs)	

	return serialized

    def work(self,**dict):
	serialized = dict['s']
	fname, fsources, args, kwargs = pickle.loads(serialized)
	fobjs = [compile(fsource, '<string>', 'exec') for fsource in fsources]

	for fobj in fobjs:
	    try:
	        eval(fobj)
	    except:
                return {'start':"failed"}	    


        __f = locals()[fname]
	try:
	    __result = __f(*args,**kwargs)
	except:
	    pass

        return {'start':__result}	    

    def __dump_funcs(self,funcs, args,**kwargs):
	"""Dumps the function and arguments
	
	"""
	sources = [self.__get_source(func) for func in funcs]
	return pickle.dumps((funcs[0].func_name,sources,args,kwargs) , \
			self.__pickle_proto)
   		   
    def __get_source(self, func):
        """Fetches source of the function"""
        #get lines of the source and adjust indent
        sourcelines = inspect.getsourcelines(func)[0]
        #remove indentation from the first line
        sourcelines[0] = sourcelines[0].lstrip()
        return "".join(sourcelines)
