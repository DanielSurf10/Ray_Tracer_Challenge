import unittest
from ray_tracer import tuple
from ray_tracer import utils


class TestTuple(unittest.TestCase):
	def test_tuple_point(self):
		t = tuple.Tuple(4.3, -4.2, 3.1, 1.0)

		self.assertAlmostEqual(t.x, 4.3, delta=utils.EPSILON)
		self.assertAlmostEqual(t.y, -4.2, delta=utils.EPSILON)
		self.assertAlmostEqual(t.z, 3.1, delta=utils.EPSILON)
		self.assertAlmostEqual(t.w, 1.0, delta=utils.EPSILON)

	def test_tuple_vector(self):
		t = tuple.Tuple(4.3, -4.2, 3.1, 0.0)

		self.assertAlmostEqual(t.x, 4.3, delta=utils.EPSILON)
		self.assertAlmostEqual(t.y, -4.2, delta=utils.EPSILON)
		self.assertAlmostEqual(t.z, 3.1, delta=utils.EPSILON)
		self.assertAlmostEqual(t.w, 0.0, delta=utils.EPSILON)

	def test_point(self):
		p = tuple.Tuple.point(4.0, -4.0, 3.0)

		self.assertAlmostEqual(p.x, 4.0, delta=utils.EPSILON)
		self.assertAlmostEqual(p.y, -4.0, delta=utils.EPSILON)
		self.assertAlmostEqual(p.z, 3.0, delta=utils.EPSILON)
		self.assertAlmostEqual(p.w, 1.0, delta=utils.EPSILON)

	def test_vector(self):
		v = tuple.Tuple.vector(4.0, -4.0, 3.0)

		self.assertAlmostEqual(v.x, 4.0, delta=utils.EPSILON)
		self.assertAlmostEqual(v.y, -4.0, delta=utils.EPSILON)
		self.assertAlmostEqual(v.z, 3.0, delta=utils.EPSILON)
		self.assertAlmostEqual(v.w, 0.0, delta=utils.EPSILON)

	def test_tuple_add(self):
		t1 = tuple.Tuple(3, -2, 5, 1)
		t2 = tuple.Tuple(-2, 3, 1, 0)

		res = t1 + t2

		self.assertAlmostEqual(res.x, 1.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, 1.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, 6.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 1.0, delta=utils.EPSILON)

	def test_point_subtraction(self):
		p1 = tuple.Tuple.point(3.0, 2.0, 1.0)
		p2 = tuple.Tuple.point(5.0, 6.0, 7.0)

		res = p1 - p2

		self.assertAlmostEqual(res.x, -2.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, -4.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, -6.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 0.0, delta=utils.EPSILON)

	def test_subtracting_vector_from_a_point(self):
		p = tuple.Tuple.point(3.0, 2.0, 1.0)
		v = tuple.Tuple.vector(5.0, 6.0, 7.0)

		res = p - v

		self.assertAlmostEqual(res.x, -2.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, -4.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, -6.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 1.0, delta=utils.EPSILON)

	def test_vector_subtraction(self):
		v1 = tuple.Tuple.vector(3.0, 2.0, 1.0)
		v2 = tuple.Tuple.vector(5.0, 6.0, 7.0)

		res = v1 - v2

		self.assertAlmostEqual(res.x, -2.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, -4.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, -6.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 0.0, delta=utils.EPSILON)

	def test_vector_subtraction_from_zero_vector(self):
		v1 = tuple.Tuple.vector(0.0, 0.0, 0.0)
		v2 = tuple.Tuple.vector(1.0, -2.0, 3.0)

		res = v1 - v2

		self.assertAlmostEqual(res.x, -1.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, 2.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, -3.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 0.0, delta=utils.EPSILON)

	def test_vector_negate(self):
		v = tuple.Tuple.vector(1.0, -2.0, 3.0)

		res = -v

		self.assertAlmostEqual(res.x, -1.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, 2.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, -3.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 0.0, delta=utils.EPSILON)

	def test_multiply_tuple_by_scalar(self):
		t = tuple.Tuple(1.0, -2.0, 3.0, -4.0)

		res = t * 3.5

		self.assertAlmostEqual(res.x, 3.5, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, -7.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, 10.5, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, -14.0, delta=utils.EPSILON)

	def test_multiply_tuple_by_fraction(self):
		t = tuple.Tuple(1.0, -2.0, 3.0, -4.0)

		res = t * 0.5

		self.assertAlmostEqual(res.x, 0.5, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, -1.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, 1.5, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, -2.0, delta=utils.EPSILON)

	def test_divide_tuple_by_scalar(self):
		t = tuple.Tuple(1.0, -2.0, 3.0, -4.0)

		res = t / 2

		self.assertAlmostEqual(res.x, 0.5, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, -1.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, 1.5, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, -2.0, delta=utils.EPSILON)

	def test_compute_magnitude_of_vector_1(self):
		v = tuple.Tuple.vector(1.0, 0.0, 0.0)

		res = v.magnitude()

		self.assertAlmostEqual(res, 1.0, delta=utils.EPSILON)

	def test_compute_magnitude_of_vector_2(self):
		v = tuple.Tuple.vector(0.0, 1.0, 0.0)

		res = v.magnitude()

		self.assertAlmostEqual(res, 1.0, delta=utils.EPSILON)

	def test_compute_magnitude_of_vector_3(self):
		v = tuple.Tuple.vector(0.0, 0.0, 1.0)

		res = v.magnitude()

		self.assertAlmostEqual(res, 1.0, delta=utils.EPSILON)

	def test_compute_magnitude_of_vector_4(self):
		v = tuple.Tuple.vector(1.0, 2.0, 3.0)

		res = v.magnitude()

		self.assertAlmostEqual(res, 14 ** 0.5, delta=utils.EPSILON)

	def test_compute_magnitude_of_vector_5(self):
		v = tuple.Tuple.vector(-1.0, -2.0, -3.0)

		res = v.magnitude()

		self.assertAlmostEqual(res, 14 ** 0.5, delta=utils.EPSILON)

	def test_normalize_vector_1(self):
		v = tuple.Tuple.vector(4.0, 0.0, 0.0)

		res = v.normalize()

		self.assertAlmostEqual(res.x, 1.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, 0.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, 0.0, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 0.0, delta=utils.EPSILON)

	def test_normalize_vector_2(self):
		v = tuple.Tuple.vector(1.0, 2.0, 3.0)
		magnitude = 14 ** 0.5

		res = v.normalize()

		self.assertAlmostEqual(res.x, 1 / magnitude, delta=utils.EPSILON)
		self.assertAlmostEqual(res.y, 2 / magnitude, delta=utils.EPSILON)
		self.assertAlmostEqual(res.z, 3 / magnitude, delta=utils.EPSILON)
		self.assertAlmostEqual(res.w, 0.0, delta=utils.EPSILON)

	def test_magnitude_of_normalized_vector(self):
		v = tuple.Tuple.vector(1.0, 2.0, 3.0)

		normalized_vector = v.normalize()
		res = normalized_vector.magnitude()

		self.assertAlmostEqual(res, 1.0, delta=utils.EPSILON)

	def test_dot_product_of_two_tuples(self):
		v1 = tuple.Tuple.vector(1.0, 2.0, 3.0)
		v2 = tuple.Tuple.vector(2.0, 3.0, 4.0)

		res = v1.dot(v2)

		self.assertAlmostEqual(res, 20.0, delta=utils.EPSILON)

	def test_cross_product_of_two_vectors(self):
		vA = tuple.Tuple.vector(1.0, 2.0, 3.0)
		vB = tuple.Tuple.vector(2.0, 3.0, 4.0)
		expected_A_B = tuple.Tuple.vector(-1.0, 2.0, -1.0)
		expected_B_A = tuple.Tuple.vector(1.0, -2.0, 1.0)

		res_A_B = vA.cross(vB)
		res_B_A = vB.cross(vA)

		# Test A x B
		self.assertAlmostEqual(res_A_B.x, expected_A_B.x, delta=utils.EPSILON)
		self.assertAlmostEqual(res_A_B.y, expected_A_B.y, delta=utils.EPSILON)
		self.assertAlmostEqual(res_A_B.z, expected_A_B.z, delta=utils.EPSILON)
		self.assertAlmostEqual(res_A_B.w, expected_A_B.w, delta=utils.EPSILON)

		# Test B x A
		self.assertAlmostEqual(res_B_A.x, expected_B_A.x, delta=utils.EPSILON)
		self.assertAlmostEqual(res_B_A.y, expected_B_A.y, delta=utils.EPSILON)
		self.assertAlmostEqual(res_B_A.z, expected_B_A.z, delta=utils.EPSILON)
		self.assertAlmostEqual(res_B_A.w, expected_B_A.w, delta=utils.EPSILON)


if __name__ == '__main__':
	unittest.main()
