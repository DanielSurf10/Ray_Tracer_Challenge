from ray_tracer import tuple, color, canvas


class Projectile:
	def __init__(self, position, velocity):
		self.position = position
		self.velocity = velocity

	def tick(self, environment):
		new_position = self.position + self.velocity
		new_velocity = self.velocity + environment.gravity + environment.wind

		return Projectile(new_position, new_velocity)


class Environment:
	def __init__(self, gravity, wind):
		self.gravity = gravity
		self.wind = wind


def print_big_pixel(image_canvas, x, y):
	pixel_size = 5

	y = (500 // pixel_size) - y

	x *= pixel_size
	y *= pixel_size
	for i in range(pixel_size):
		for j in range(pixel_size):
			image_canvas.write_pixel(x + i, y + j, color.Color(1, 1, 1))


def create_parable(image_canvas):
	ticks = 0
	proj = Projectile(tuple.Tuple.point(0, 1, 0), tuple.Tuple.vector(1, 1.8, 0).normalize() * 5)
	env = Environment(tuple.Tuple.vector(0, -0.1, 0), tuple.Tuple.vector(-0.01, 0, 0))

	while proj.position.y > 0:
		proj = proj.tick(env)
		print_big_pixel(image_canvas, int(proj.position.x), int(proj.position.y))
		ticks += 1


if __name__ == '__main__':
	image_canvas = canvas.Canvas(900, 500)
	create_parable(image_canvas)

	ppm_data = image_canvas.canvas_to_ppm()
	with open('parable.ppm', 'w') as ppm_file:
		ppm_file.write(ppm_data)
