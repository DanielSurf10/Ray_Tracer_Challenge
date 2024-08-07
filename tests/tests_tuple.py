import unittest
from ray_tracer.tuple import Tuple
from ray_tracer.utils import compare_float

class TestTuple(unittest.TestCase):
	def test_tuple_1(self):
		t = Tuple(4.3, -4.2, 3.1, 1.0)
		self.assertTrue(compare_float(t.x, 4.3))
		self.assertTrue(compare_float(t.y, -4.2))
		self.assertTrue(compare_float(t.z, 3.1))
		self.assertTrue(compare_float(t.w, 1.0))

	def test_tuple_2(self):
		t = Tuple(4.3, -4.2, 3.1, 0.0)
		self.assertTrue(compare_float(t.x, 4.3))
		self.assertTrue(compare_float(t.y, -4.2))
		self.assertTrue(compare_float(t.z, 3.1))
		self.assertTrue(compare_float(t.w, 0.0))

if __name__ == '__main__':
	unittest.main()
