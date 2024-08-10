import math


class Tuple:
	def __init__(self, x: float, y: float, z: float, w: float):
		self.x = x
		self.y = y
		self.z = z
		self.w = w

	@staticmethod
	def point(x: float, y: float, z: float):
		return Tuple(x, y, z, 1.0)

	@staticmethod
	def vector(x: float, y: float, z: float):
		return Tuple(x, y, z, 0.0)

	def add(self, other: 'Tuple'):
		return Tuple(self.x + other.x,
					 self.y + other.y,
					 self.z + other.z,
					 self.w + other.w)

	def __add__(self, other: 'Tuple'):
		return self.add(other)

	def sub(self, other: 'Tuple'):
		return Tuple(self.x - other.x,
					 self.y - other.y,
					 self.z - other.z,
					 self.w - other.w)

	def __sub__(self, other: 'Tuple'):
		return self.sub(other)

	def negate(self):
		return Tuple(-self.x, -self.y, -self.z, -self.w)

	def __neg__(self):
		return self.negate()

	def mul(self, multiplier):
		if isinstance(multiplier, float) or isinstance(multiplier, int):
			return Tuple(self.x * multiplier,
						 self.y * multiplier,
						 self.z * multiplier,
						 self.w * multiplier)
		# elif isinstance(scalar, Matrix):
		# 	# Perform matrix multiplication
		# 	# Your code here
		else:
			raise TypeError("Unsupported operand type for multiplication")

	def __mul__(self, scalar: float):
		return self.mul(scalar)

	def div(self, divisor):
		if isinstance(divisor, float) or isinstance(divisor, int):
			if divisor != 0:
				return Tuple(self.x / divisor,
				 			 self.y / divisor,
							 self.z / divisor,
							 self.w / divisor)
			else:
				raise ZeroDivisionError("Division by zero is not allowed")
		else:
			raise TypeError("Unsupported operand type for division")

	def __truediv__(self, divisor):
		return self.div(divisor)

	def magnitude(self):
		return math.sqrt(self.x ** 2 +
						 self.y ** 2 +
						 self.z ** 2 +
						 self.w ** 2)

	def normalize(self):
		magnitude = self.magnitude()
		return Tuple(self.x / magnitude,
					 self.y / magnitude,
					 self.z / magnitude,
					 self.w / magnitude)

	def dot(self, other: 'Tuple'):
		return (self.x * other.x +
				self.y * other.y +
				self.z * other.z +
				self.w * other.w)

	def cross(self, other: 'Tuple'):
		return Tuple.vector(self.y * other.z - self.z * other.y,
							self.z * other.x - self.x * other.z,
							self.x * other.y - self.y * other.x)
