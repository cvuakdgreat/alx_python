"""	Creating a Class called BaseGeometry"""
class BaseGeometry:
	""" Class called Base Geometry"""
	def area(self):
		""" method that raises a Exception"""
		raise Exception("area() is not implemented")
	
	def integer_validator(self, name, value):
		if not isinstance(value, int):
			raise TypeError("{} must be an integer".format(value))
		if value <= 0 :
			raise ValueError("{} must be greater than 0".format(value))
	

