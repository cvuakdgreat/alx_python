""" creating a function """ 
def is_same_class(obj, a_class):
	"""Function that returns True or false if the object is exactly an instance of the specified class """ 
	return type(obj) == a_class

	def ignore_init_subclass_methods(cls):
    # Define a function to filter out methods starting with '__init_subclass__'
	    return [attr for attr in dir('cls') if not attr.startswith('__init_subclass__')]