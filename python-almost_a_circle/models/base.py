"""
	This module generates id
"""

class Base:
	"""
	Class called base
	arg:
		__nb_objects: private attribute with an initial value of 0 
	
	"""
	__nb_objects = 0;
	def __init__(self, id=None):
		"""
		This init method return id if defined and if not defined

		args:
			id (int): it is a public variable, and it is either defined or assigned
		"""
		if not id == None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects