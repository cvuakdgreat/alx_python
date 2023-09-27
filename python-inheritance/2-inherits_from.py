""" creating a function """ 

def inherits_from(obj, a_class):
	"""Function that returns True or false if the object is an instance of a class that inherited (directly or indirectly) from the specified class ;""" 	
	if not issubclass(obj, a_class):
		return False
	else:
		return True