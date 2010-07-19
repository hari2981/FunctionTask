from pydra.cluster.controller.web.controller import WebController
from pydra.cluster.controller import ControllerException
from pydra.config import load_settings 
from task.FunctionTask import FunctionTask

class FunctionClient(WebController):
    """
    Controller for interacting with functions
    """
    def __init__(self,globals_list):
	self.F = FunctionTask(globals_list)
	settings = load_settings()
        self.pydra_controller = WebController(settings.HOST, \
			     	settings.CONTROLLER_PORT,
				key='%s/master.key' % settings.RUNTIME_FILES_DIR)
	
    def __getattribute__(self,key):
    	return object.__getattribute__(self,key)	    

    def run(self, func, args, **kwargs):
	serialized = self.F.serialize(func,args,**kwargs)
	try:
#	    self.pydra_controller.queue_task('task.FunctionTask.FunctionTask', \
#			    {'s':serialized}) 
	    task_instance = self.pydra_controller.queue_task('demo.demo_task.TestTask', \
			    {'start':5}) 
	    self.task_id = task_instance['instance_id']
	    	

        except ControllerException, e:
	    error = e.code

    def result(self):
        while 1:			
      	    task_history = self.pydra_controller.task_history_detail(self.task_id)
	    if task_history['details']['results']:	
	        return task_history['details']['results']['start']	
 	    
