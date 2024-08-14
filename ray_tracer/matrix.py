from ray_tracer import utils
from ray_tracer import tuple


class Matrix:
	def __init__(self, width, high):
		self.width = width
		self.high = high
		self.data = [float(0) for _ in range(width * high)]

	@classmethod
	def from_list(cls, width, high, data):
		matrix = cls(width, high)
		matrix.data = data[:]
		return matrix

	@classmethod
	def identity(cls, width, high):
		result = cls(width, high)

		for y in range(high):
			for x in range(width):
				if x == y:
					result.set(y, x, 1)
				else:
					result.set(y, x, 0)

		return (result)

	def get(self, y, x):
		return self.data[x + y * self.width]

	def set(self, y, x, value):
		self.data[x + y * self.width] = value

	def is_equal(self, other):
		if (self.width != other.width) or (self.high != other.high):
			return False

		for i in range(len(self.data)):
			if not utils.compare_float(self.data[i], other.data[i]):
				return False
		return True

	def multiply(self, other):
		result = Matrix(self.width, other.high)

		for y in range(result.high):
			for x in range(result.width):
				value = 0
				for i in range(result.width):
					value += self.get(y, i) * other.get(i, x)
				result.set(y, x, value)

		return result

	def multiply_by_tuple(self, tuple_data: 'tuple.Tuple'):
		if self.width != 4:
			raise ValueError("Tuple size does not match matrix width")

		tuple_data_list = [tuple_data.x, tuple_data.y, tuple_data.z, tuple_data.w]
		tuple_result = [0] * 4

		for i in range(4):
			value = self.get(i, 0) * tuple_data_list[0] \
					+ self.get(i, 1) * tuple_data_list[1] \
					+ self.get(i, 2) * tuple_data_list[2] \
					+ self.get(i, 3) * tuple_data_list[3]
			tuple_result[i] = value

		result = tuple.Tuple(*tuple_result)
		return (result)

	def transpose(self):
		result = Matrix(self.high, self.width)

		for y in range(self.high):
			for x in range(self.width):
				result.set(x, y, self.get(y, x))

		return result

	def determinant(self):
		result = 0

		if self.width == 2 and self.high == 2:
			result = self.get(0, 0) * self.get(1, 1) \
						- self.get(0, 1) * self.get(1, 0)
			return result

		elif self.width == 3 and self.high == 3:
			result = self.get(0, 0) * self.get(1, 1) * self.get(2, 2) \
						+ self.get(0, 1) * self.get(1, 2) * self.get(2, 0) \
						+ self.get(0, 2) * self.get(1, 0) * self.get(2, 1) \
						- self.get(0, 2) * self.get(1, 1) * self.get(2, 0) \
						- self.get(0, 1) * self.get(1, 0) * self.get(2, 2) \
						- self.get(0, 0) * self.get(1, 2) * self.get(2, 1)

		return result

	def submatrix(self, y: int, x: int):
		result = Matrix(self.width - 1, self.high - 1)
		aux_tuple = tuple.Tuple(0, 0, 0, 0)

		for i in range(self.high):
			if i == y:
				continue
			for j in range(self.width):
				if j == x:
					continue

				aux_tuple.y = i - 1 if i > y else i
				aux_tuple.x = j - 1 if j > x else j

				result.set(aux_tuple.y, aux_tuple.x, self.get(i, j))

		return result
