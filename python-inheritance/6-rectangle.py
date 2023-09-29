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

"""creating a class called Rectangle"""

class Rectangle(BaseGeometry):
	def __init__(self, width, height):
		self.__width = 0
		self.__height = 0
		self.integer_validator("width", width)
		self.integer_validator("height", height)
		self.__width = width
		self.__height = height


