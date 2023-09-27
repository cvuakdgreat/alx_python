"""	Creating a Class"""
class BaseGeometry:
	""" Class called Base Geometry"""
	def area(self):
		""" method that raises a Exception"""
		raise Exception("area() is not implemented")
	
if '__init_subclass__' in dir(BaseGeometry):
    dir(BaseGeometry).remove('__init_subclass__')
	

