import unittest
from ray_tracer.tuple import Tuple

class TestTuple(unittest.TestCase):
	def test_tuple_1(self):
		t = Tuple(4.3, -4.2, 3.1, 1.0)
		self.assertEqual(t.x, 4.3)
		self.assertEqual(t.y, -4.2)
		self.assertEqual(t.z, 3.1)
		self.assertEqual(t.w, 1.0)

	def test_tuple_2(self):
		t = Tuple(4.3, -4.2, 3.1, 0.0)
		self.assertEqual(t.x, 4.3)
		self.assertEqual(t.y, -4.2)
		self.assertEqual(t.z, 3.1)
		self.assertEqual(t.w, 1.0)

if __name__ == '__main__':
	unittest.main()
