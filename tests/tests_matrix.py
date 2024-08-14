import unittest
from ray_tracer import matrix
from ray_tracer import tuple
from ray_tracer import utils


class TestMatrix(unittest.TestCase):
	def test_matrix(self):
		data = [
				1, 2, 3, 4,
				5.5, 6.5, 7.5, 8.5,
				9, 10, 11, 12,
				13.5, 14.5, 15.5, 16.5
		]

		m = matrix.Matrix.from_list(4, 4, data)

		self.assertAlmostEqual(m.get(0, 0), 1, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(0, 3), 4, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(1, 0), 5.5, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(1, 2), 7.5, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(2, 2), 11, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(3, 0), 13.5, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(3, 2), 15.5, delta=utils.EPSILON)

	def test_matrix_2x2(self):
		data = [
				-3, 5,
				1, -2
		]

		m = matrix.Matrix.from_list(2, 2, data)

		self.assertAlmostEqual(m.get(0, 0), -3, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(0, 1), 5, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(1, 0), 1, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(1, 1), -2, delta=utils.EPSILON)

	def test_matrix_3x3(self):
		data = [
				-3, 5, 0,
				1, -2, -7,
				0, 1, 1
		]

		m = matrix.Matrix.from_list(3, 3, data)

		self.assertAlmostEqual(m.get(0, 0), -3, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(1, 1), -2, delta=utils.EPSILON)
		self.assertAlmostEqual(m.get(2, 2), 1, delta=utils.EPSILON)

	def test_matrix_equality(self):
		data = [
				1, 2, 3, 4,
				5, 6, 7, 8,
				9, 8, 7, 6,
				5, 4, 3, 2
		]

		m1 = matrix.Matrix.from_list(4, 4, data)
		m2 = matrix.Matrix.from_list(4, 4, data)

		self.assertTrue(m1.is_equal(m2))

	def test_matrix_inequality(self):
		data1 = [
				1, 2, 3, 4,
				5, 6, 7, 8,
				9, 8, 7, 6,
				5, 4, 3, 2
		]

		data2 = [
				2, 3, 4, 5,
				6, 7, 8, 9,
				8, 7, 6, 5,
				4, 3, 2, 1
		]

		m1 = matrix.Matrix.from_list(4, 4, data1)
		m2 = matrix.Matrix.from_list(4, 4, data2)

		self.assertFalse(m1.is_equal(m2))

	def test_matrix_multiplication(self):
		data1 = [
				1, 2, 3, 4,
				5, 6, 7, 8,
				9, 8, 7, 6,
				5, 4, 3, 2
		]

		data2 = [
				-2, 1, 2, 3,
				3, 2, 1, -1,
				4, 3, 6, 5,
				1, 2, 7, 8
		]

		expected = [
				20, 22, 50, 48,
				44, 54, 114, 108,
				40, 58, 110, 102,
				16, 26, 46, 42
		]

		m1 = matrix.Matrix.from_list(4, 4, data1)
		m2 = matrix.Matrix.from_list(4, 4, data2)
		expected_matrix = matrix.Matrix.from_list(4, 4, expected)

		result = m1.multiply(m2)

		self.assertTrue(result.is_equal(expected_matrix))

	def test_matrix_multiplication_tuple(self):
		data1 = [
				1, 2, 3, 4,
				2, 4, 4, 2,
				8, 6, 4, 1,
				0, 0, 0, 1
		]

		tuple1 = tuple.Tuple(1, 2, 3, 1)
		m1 = matrix.Matrix.from_list(4, 4, data1)

		result = m1.multiply_by_tuple(tuple1)

		self.assertAlmostEqual(result.x, 18, delta=utils.EPSILON)
		self.assertAlmostEqual(result.y, 24, delta=utils.EPSILON)
		self.assertAlmostEqual(result.z, 33, delta=utils.EPSILON)
		self.assertAlmostEqual(result.w, 1, delta=utils.EPSILON)

	def test_matrix_identity(self):
		data = [
			1, 0, 0, 0,
			0, 1, 0, 0,
			0, 0, 1, 0,
			0, 0, 0, 1
		]

		expected_matrix = matrix.Matrix.from_list(4, 4, data)

		result = matrix.Matrix.identity(4, 4)

		self.assertTrue(expected_matrix.is_equal(result))

	def test_matrix_multiplication_identity(self):
		data = [
			0, 1, 2, 4,
			1, 2, 4, 8,
			2, 4, 8, 16,
			4, 8, 16, 32
		]

		m1 = matrix.Matrix.from_list(4, 4, data)
		m2 = matrix.Matrix.identity(4, 4)

		result = m1.multiply(m2)

		self.assertTrue(m1.is_equal(result))

	def test_matrix_transpose(self):
		data = [
			0, 9, 3, 0,
			9, 8, 0, 8,
			1, 8, 5, 3,
			0, 0, 5, 8
		]

		expected_data = [
			0, 9, 1, 0,
			9, 8, 8, 0,
			3, 0, 5, 5,
			0, 8, 3, 8
		]

		m = matrix.Matrix.from_list(4, 4, data)
		expected_matrix = matrix.Matrix.from_list(4, 4, expected_data)

		result = m.transpose()

		self.assertTrue(expected_matrix.is_equal(result))

	def test_matrix_transpose_identity(self):
		m = matrix.Matrix.identity(4, 4)

		result = m.transpose()

		self.assertTrue(m.is_equal(result))

	def test_matrix_determinant_2x2(self):
		data = [
			1, 5,
			-3, 2
		]

		m = matrix.Matrix.from_list(2, 2, data)

		result = m.determinant()

		self.assertAlmostEqual(result, 17, delta=utils.EPSILON)

	def test_matrix_submatrix_3x3(self):
		data = [
			1, 5, 0,
			-3, 2, 7,
			0, 6, -3
		]

		expected_data = [
			-3, 2,
			0, 6
		]

		m = matrix.Matrix.from_list(3, 3, data)
		expected_matrix = matrix.Matrix.from_list(2, 2, expected_data)

		result = m.submatrix(0, 2)

		self.assertTrue(expected_matrix.is_equal(result))

# 	def test_matrix_submatrix_4x4(self):
# 		data = [
# 			-6, 1, 1, 6,
# 			-8, 5, 8, 6,
# 			-1, 0, 8, 2,
# 			-7, 1, -1, 1
# 		]
#
# 		expected_data = [
# 			-6, 1, 6,
# 			-8, 8, 6,
# 			-7, -1, 1
# 		]
#
# 		m = matrix.Matrix.from_list(4, 4, data)
# 		expected_matrix = matrix.Matrix.from_list(3, 3, expected_data)
#
# 		result = m.submatrix(2, 1)
#
# 		self.assertTrue(expected_matrix.is_equal(result))
#
# 	def test_matrix_minor_3x3(self):
# 		data = [
# 			3, 5, 0,
# 			2, -1, -7,
# 			6, -1, 5
# 		]
#
# 		m = matrix.Matrix.from_list(3, 3, data)
# 		submatrix = m.submatrix(1, 0)
#
# 		result = submatrix.determinant()
#
# 		self.assertAlmostEqual(result, 25, delta=utils.EPSILON)
#
# 	def test_matrix_cofactor_3x3(self):
# 		data = [
# 			3, 5, 0,
# 			2, -1, -7,
# 			6, -1, 5
# 		]
#
# 		m = matrix.Matrix.from_list(3, 3, data)
#
# 		result1 = m.minor(0, 0)
# 		result2 = m.cofactor(0, 0)
# 		result3 = m.minor(1, 0)
# 		result4 = m.cofactor(1, 0)
#
# 		self.assertAlmostEqual(result1, -12, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result2, -12, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result3, 25, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result4, -25, delta=utils.EPSILON)

# 	def test_matrix_determinant_3x3(self):
# 		data = [
# 			1, 2, 6,
# 			-5, 8, -4,
# 			2, 6, 4
# 		]
#
# 		m = matrix.Matrix.from_list(3, 3, data)
#
# 		result1 = m.cofactor(0, 0)
# 		result2 = m.cofactor(0, 1)
# 		result3 = m.cofactor(0, 2)
#
# 		self.assertAlmostEqual(result1, 56, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result2, 12, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result3, -46, delta=utils.EPSILON)
# 		self.assertAlmostEqual(m.determinant(), -196, delta=utils.EPSILON)

# 	def test_matrix_determinant_4x4(self):
# 		data = [
# 			-2, -8, 3, 5,
# 			-3, 1, 7, 3,
# 			1, 2, -9, 6,
# 			-6, 7, 7, -9
# 		]
#
# 		m = matrix.Matrix.from_list(4, 4, data)
#
# 		result1 = m.cofactor(0, 0)
# 		result2 = m.cofactor(0, 1)
# 		result3 = m.cofactor(0, 2)
# 		result4 = m.cofactor(0, 3)
#
# 		self.assertAlmostEqual(result1, 690, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result2, 447, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result3, 210, delta=utils.EPSILON)
# 		self.assertAlmostEqual(result4, 51, delta=utils.EPSILON)
# 		self.assertAlmostEqual(m.determinant(), -4071, delta=utils.EPSILON)
#
# 	def test_matrix_invertible(self):
# 		data = [
# 			6, 4, 4, 4,
# 			5, 5, 7, 6,
# 			4, -9, 3, -7,
# 			9, 1, 7, -6
# 		]
#
# 		m = matrix.Matrix.from_list(4, 4, data)
# 		determinant = m.determinant()
#
# 		self.assertAlmostEqual(determinant, -2120, delta=utils.EPSILON)
# 		self.assertTrue(determinant != 0)
#
# 	def test_matrix_not_invertible(self):
# 		data = [
# 			-4, 2, -2, -3,
# 			9, 6, 2, 6,
# 			0, -5, 1, -5,
# 			0, 0, 0, 0
# 		]
#
# 		m = matrix.Matrix.from_list(4, 4, data)
# 		determinant = m.determinant()
#
# 		self.assertAlmostEqual(determinant, 0, delta=utils.EPSILON)
# 		self.assertTrue(determinant == 0)
#
# 	def test_matrix_inverse(self):
# 		data = [
# 			-5, 2, 6, -8,
# 			1, -5, 1, 8,
# 			7, 7, -6, -7,
# 			1, -3, 7, 4
# 		]
#
# 		expected_data = [
# 			0.21805, 0.45113, 0.24060, -0.04511,
# 			-0.80827, -1.45677, -0.44361, 0.52068,
# 			-0.07895, -0.22368, -0.05263, 0.19737,
# 			-0.52256, -0.81391, -0.30075, 0.30639
# 		]
#
# 		m = matrix.Matrix.from_list(4, 4, data)
# 		expected_matrix = matrix.Matrix.from_list(4, 4, expected_data)
# 		determinant = m.determinant()
# 		inverse = m.inverse()
#
# 		self.assertAlmostEqual(determinant, 532, delta=utils.EPSILON)
# 		self.assertAlmostEqual(m.cofactor(2, 3), -160, delta=utils.EPSILON)
# 		self.assertAlmostEqual(inverse.get(3, 2), -160/532, delta=utils.EPSILON)
# 		self.assertAlmostEqual(m.cofactor(3, 2), 105, delta=utils.EPSILON)
# 		self.assertAlmostEqual(inverse.get(2, 3), 105/532, delta=utils.EPSILON)
# 		self.assertTrue(expected_matrix.is_equal(inverse))
#
# 	def test_matrix_inverse_2(self):
# 		data = [
# 			8, -5, 9, 2,
# 			7, 5, 6, 1,
# 			-6, 0, 9, 6,
# 			-3, 0, -9, -4
# 		]
#
# 		expected_data = [
# 			-0.15385, -0.15385, -0.28205, -0.53846,
# 			-0.07692, 0.12308, 0.02564, 0.03077,
# 			0.35897, 0.35897, 0.43590, 0.92308,
# 			-0.69231, -0.69231, -0.76923, -1.92308
# 		]
#
# 		m = matrix.Matrix.from_list(4, 4, data)
# 		expected_matrix = matrix.Matrix.from_list(4, 4, expected_data)
# 		inverse = m.inverse()
#
# 		self.assertTrue(expected_matrix.is_equal(inverse))
#
# 	def test_matrix_inverse_3(self):
# 		data = [
# 			9, 3, 0, 9,
# 			-5, -2, -6, -3,
# 			-4, 9, 6, 4,
# 			-7, 6, 6, 2
# 		]
#
# 		expected_data = [
# 			-0.04074, -0.07778, 0.14444, -0.22222,
# 			-0.07778, 0.03333, 0.36667, -0.33333,
# 			-0.02901, -0.14630, -0.10926, 0.12963,
# 			0.17778, 0.06667, -0.26667, 0.33333
# 		]
#
# 		m = matrix.Matrix.from_list(4, 4, data)
# 		expected_matrix = matrix.Matrix.from_list(4, 4, expected_data)
# 		inverse = m.inverse()
#
# 		self.assertTrue(expected_matrix.is_equal(inverse))
#
# 	def test_matrix_inverse_multiply(self):
# 		data1 = [
# 			3, -9, 7, 3,
# 			3, -8, 2, -9,
# 			-4, 4, 4, 1,
# 			-6, 5, -1, 1
# 		]
#
# 		data2 = [
# 			8, 2, 2, 2,
# 			3, -1, 7, 0,
# 			7, 0, 5, 4,
# 			6, -2, 0, 5
# 		]
#
# 		m1 = matrix.Matrix.from_list(4, 4, data1)
# 		m2 = matrix.Matrix.from_list(4, 4, data2)
# 		m3 = m1.multiply(m2)
# 		m4 = m3.multiply(m2.inverse())
#
# 		self.assertTrue(m1.is_equal(m4))


if __name__ == '__main__':
	unittest.main()
