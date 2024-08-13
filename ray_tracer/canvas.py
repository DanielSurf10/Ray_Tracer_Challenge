from ray_tracer import color
import math


class Canvas:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.pixels = [color.Color(0, 0, 0) for _ in range(width * height)]

	def write_pixel(self, x, y, color):
		self.pixels[x + y * self.width] = color

# 	def __getitem__(self, index):
# 		start = index * self.width
# 		end = (index + 1) * self.width
#
# 		return [self.pixels[i] for i in range(start, end)]
#
# 	def pixel_at(self, x, y):
# 		return self.pixels[y][x]

	def pixel_at(self, x, y):
		return self.pixels[x + y * self.width]

	@staticmethod
	def convert_color(color):
		new_color = math.ceil(color * 255)
		return min(255, max(0, new_color))

	def canvas_to_ppm(self):
		magic_number = 'P3'
		width = str(self.width)
		height = str(self.height)

		header = f'{magic_number}\n{width} {height}\n255\n'

		data = []
		for pixel in self.pixels:
			line = f'{Canvas.convert_color(pixel.red)} ' \
				   f'{Canvas.convert_color(pixel.green)} ' \
				   f'{Canvas.convert_color(pixel.blue)}'
			data.append(line)

		lines = []
		for i in range(0, len(data), self.width):
			lines.append(' '.join(data[i:i + self.width]))

		result = header + '\n'.join(lines) + '\n'
		return result
