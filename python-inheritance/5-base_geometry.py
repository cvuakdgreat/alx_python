"""	Creating a Class called BaseGeometry"""
class BaseGeometry:
	""" Class called Base Geometry"""
	def __init__(self):
		pass
	
	def area(self):
		""" method that raises a Exception"""
		raise Exception("area() is not implemented")
	
	def integer_validator(self, name, value):
		""" Method that validates intergers
		
			args:
				value 

			return:
				TypeError
				valueError
		"""
		if not isinstance(value, int):
			raise TypeError("{} must be an integer".format(name))
		if value <= 0 :
			raise ValueError("{} must be greater than 0".format(name))
	