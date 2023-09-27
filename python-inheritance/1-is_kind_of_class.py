""" creating a function """ 

def is_kind_of_class(obj, a_class):
	"""Function that returns True or false if the object is exactly an instance of the specified class or Inherited class""" 	
	if isinstance(obj) == a_class:
		return True
	elif type(obj) == a_class:
		return True
	else:
		return False
	