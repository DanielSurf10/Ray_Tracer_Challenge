import unittest
from ray_tracer import color
from ray_tracer import canvas
from ray_tracer import utils
import sys


class TestColor(unittest.TestCase):
	def test_color(self):
		c = color.Color(-0.5, 0.4, 1.7)

		self.assertAlmostEqual(c.red, -0.5, delta=utils.EPSILON)
		self.assertAlmostEqual(c.green, 0.4, delta=utils.EPSILON)
		self.assertAlmostEqual(c.blue, 1.7, delta=utils.EPSILON)

	def test_color_add(self):
		c1 = color.Color(0.9, 0.6, 0.75)
		c2 = color.Color(0.7, 0.1, 0.25)

		c = c1 + c2

		self.assertAlmostEqual(c.red, 1.6, delta=utils.EPSILON)
		self.assertAlmostEqual(c.green, 0.7, delta=utils.EPSILON)
		self.assertAlmostEqual(c.blue, 1.0, delta=utils.EPSILON)

	def test_color_sub(self):
		c1 = color.Color(0.9, 0.6, 0.75)
		c2 = color.Color(0.7, 0.1, 0.25)

		c = c1 - c2

		self.assertAlmostEqual(c.red, 0.2, delta=utils.EPSILON)
		self.assertAlmostEqual(c.green, 0.5, delta=utils.EPSILON)
		self.assertAlmostEqual(c.blue, 0.5, delta=utils.EPSILON)

	def test_color_mul(self):
		c = color.Color(0.2, 0.3, 0.4)
		scalar = 2

		c = c * scalar

		self.assertAlmostEqual(c.red, 0.4, delta=utils.EPSILON)
		self.assertAlmostEqual(c.green, 0.6, delta=utils.EPSILON)
		self.assertAlmostEqual(c.blue, 0.8, delta=utils.EPSILON)

	def test_color_mul_hadamard(self):
		c1 = color.Color(1, 0.2, 0.4)
		c2 = color.Color(0.9, 1, 0.1)

		c = c1 * c2

		self.assertAlmostEqual(c.red, 0.9, delta=utils.EPSILON)
		self.assertAlmostEqual(c.green, 0.2, delta=utils.EPSILON)
		self.assertAlmostEqual(c.blue, 0.04, delta=utils.EPSILON)

	def test_canvas(self):
		c = canvas.Canvas(10, 20)

		self.assertEqual(c.width, 10)
		self.assertEqual(c.height, 20)

		for pixel in c.pixels:
			self.assertAlmostEqual(pixel.red, 0, delta=utils.EPSILON)
			self.assertAlmostEqual(pixel.green, 0, delta=utils.EPSILON)
			self.assertAlmostEqual(pixel.blue, 0, delta=utils.EPSILON)

	def test_write_pixel(self):
		c = canvas.Canvas(10, 20)
		red = color.Color(1, 0, 0)

		c.write_pixel(2, 3, red)

		pixel = c.pixel_at(2, 3)
		self.assertAlmostEqual(pixel.red, 1, delta=utils.EPSILON)
		self.assertAlmostEqual(pixel.green, 0, delta=utils.EPSILON)
		self.assertAlmostEqual(pixel.blue, 0, delta=utils.EPSILON)

	def test_canvas_to_ppm(self):
		c = canvas.Canvas(5, 3)
		c1 = color.Color(1.5, 0, 0)
		c2 = color.Color(0, 0.5, 0)
		c3 = color.Color(-0.5, 0, 1)

		c.write_pixel(0, 0, c1)
		c.write_pixel(2, 1, c2)
		c.write_pixel(4, 2, c3)

		ppm = c.canvas_to_ppm()

		self.assertEqual(ppm, 'P3\n5 3\n255\n' +
								'255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n' +
								'0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n' +
								'0 0 0 0 0 0 0 0 0 0 0 0 0 0 255\n')


if __name__ == '__main__':
	unittest.main()
