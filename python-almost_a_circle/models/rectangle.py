"""
Module importing a class for a module
"""

from models.base import Base

"""
Rectangle Module
"""

class Rectangle(Base):
	"""
		A sub class inheriting from Super class Base,
		Creating a class representing Rectangle
	"""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""
		Class constructor method
		Initializes a Rectangle instance


		Args:
			width int: width of the rectangle
			height int: height of the ectangle
			x int: X-coordinate of the rectangle
			y int: y-coordinate of the rectangle
			id int: ID of the rectangle

		"""
		
		super().__init__(id)
		if type(width) is not int:
			raise TypeError("width must be an integer")
		elif width <= 0:
			raise ValueError("width must be > 0")
		else:
			self.__width = width

		if type(height) is not int:
			raise TypeError("height must be an integer")
		elif height <= 0:
			raise ValueError("height must be > 0")
		else:
			self.__height = height

		if type(x) is not int:
			raise TypeError("x must be an integer")
		elif x < 0:
			raise ValueError("x must be >= 0")
		else:
			self.__x = x

		if type(y) is not int:
			raise TypeError("y must be an integer")
		elif y < 0:
			raise ValueError("y must be >= 0")
		else:
			self.__y = y
	
		
	@property
	def width(self):
		"""
		Getter method for width attribute.

		Returns:
			int: The width of the rectangle.
		"""
		return self.__width
	
	@width.setter
	def width(self, value):

		"""
		Setter method for width attribute.

		Args:
			value (int): The width to set.

		Raises:
			TypeError: if value not int
			ValueError: If value is not an integer greater than 0.
		"""
		if not isinstance(value, int):
			raise TypeError('width must be an integer')
		elif value <= 0 :
			raise ValueError('width must be > 0')
		else:
			self.__width = value
		
	@property
	def height(self):
		"""
		Getter method for height attribute.

		Returns:
			int: The height of the rectangle.
		"""
		return self.__height
	
	@height.setter
	def height(self, value):

		"""
		Setter method for height attribute.

		Args:
			value (int): The height to set.

		Raises:
			TypeError: if value not int
			ValueError: If value is not an integer greater than 0.
		"""
		if not isinstance(value, int):
			raise TypeError('height must be an integer')
		elif value <= 0 :
			raise ValueError('height must be > 0')
		else:
			self.__height = value

	@property
	def x(self):
		"""
		Getter method for x attribute.

		Returns:
			int: The x of the rectangle.
		"""
		return self.__x
	
	@x.setter
	def x(self, value):

		"""
		Setter method for x attribute.

		Args:
			value (int): The x to set.

		Raises:
			TypeError: if value not int
			ValueError: If value is not an integer greater than 0.
		"""
		if not isinstance(value, int):
			raise TypeError('x must be an integer')
		elif value < 0 :
			raise ValueError('x must be >= 0')
		else:
			self.__x = value

	@property
	def y(self):
		"""
		Getter method for y attribute.

		Returns:
			int: The y of the rectangle.
		"""
		return self.__y
	
	@y.setter
	def y(self, value):

		"""
		Setter method for y attribute.

		Args:
			value (int): The y to set.

		Raises:
			TypeError: if value not int
			ValueError: If value is not an integer greater than 0.
		"""
		if not isinstance(value, int):
			raise TypeError('y must be an integer')
		elif value < 0 :
			raise ValueError('y must be >= 0')
		else:
			self.__y = value
	
	def area(self):
		"""
			method that returns the multiplication of width and height or Area
		"""
		return self.__width * self.__height
	
	def display(self):
		"""
			method that represents a rectangle with #
		"""
		for _ in range(self.__y):
			print()
		for _ in range(self.__height):
			print(" " * self.__x + "#" * self.__width)

	def __str__(self):
		""""
		Method to overwrite the __str__ return
		"""
		return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

	def update(self, *args, **kwargs):
		"""
		Method assigns argunments to each attributes
		"""

		args_length = len(args)
		kwargs_lenght = len(kwargs)


		if args_length > 0:
			self.id = args[0]
		if args_length > 1:
			self.width = args[1]
		if args_length > 2:
			self.height = args[2]

		if args_length > 3:
			self.x = args[3]
		if args_length > 4:
			self.y = args[4]

		for key, value in kwargs.items():
			if key == "id":
				self.id= value
			elif key == "width":
				self.width = value
			elif key == "height":
				self.height = value
			elif key == "x":
				self.x = value
			elif key == "y":
				self.y = value

