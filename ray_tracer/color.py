class Color:
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue

	def add(self, other):
		return Color(self.red + other.red,
					 self.green + other.green,
					 self.blue + other.blue)

	def __add__(self, other):
		return self.add(other)

	def sub(self, other):
		return Color(self.red - other.red,
					 self.green - other.green,
					 self.blue - other.blue)

	def __sub__(self, other):
		return self.sub(other)

	def mul_scalar(self, scalar):
		return Color(self.red * scalar,
					 self.green * scalar,
					 self.blue * scalar)

	def mul_hadamard(self, other):
		return Color(self.red * other.red,
					 self.green * other.green,
					 self.blue * other.blue)

	def __mul__(self, other):
		if isinstance(other, Color):
			return self.mul_hadamard(other)
		else:
			return self.mul_scalar(other)
