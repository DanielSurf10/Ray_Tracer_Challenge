import sys
sys.path.append('/home/daniel/Documentos/GitHub/Ray_Tracer_Challenge')

from ray_tracer import tuple


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


if __name__ == '__main__':
	ticks = 0
	proj = Projectile(tuple.Tuple.point(0, 1, 0), tuple.Tuple.vector(1, 1, 0))
	env = Environment(tuple.Tuple.vector(0, -0.1, 0), tuple.Tuple.vector(-0.01, 0, 0))

	while proj.position.y > 0:
		proj = proj.tick(env)
		print(f'{ticks:2d} - pos: x = {proj.position.x:5.2f} - y = {proj.position.y:5.2f} - z = {proj.position.z:5.2f}')
		ticks += 1
