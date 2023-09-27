"""
	Creating a Class
"""

class BaseGeometry:
	""" Class called Base Geometry"""
	def __init__(self) :
		pass

	def area(self):
		""" method that raises a Exception"""
		raise ValueError("area() is not implemented")