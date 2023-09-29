""" getting BaseGeometry Class for the module 5-base_geometry """

from 5-base_geometry import BaseGeometry

"""creating a class called Rectangle"""

class Rectangle(BaseGeometry):
	def __init__(self, width, height):
		self.__width = 0
		self.__height = 0
		self.integer_validator("width", width)
		self.integer_validator("height", height)
		self.__width = width
		self.__height = height


