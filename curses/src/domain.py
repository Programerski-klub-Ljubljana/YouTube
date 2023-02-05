class Plosca:
	simbol = '='
	def __init__(self, x, y, sirina):
		self.x = x
		self.y = y
		self.sirina = sirina

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

class Zoga:

	simbol = 'o'

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.hitrost_x = -1
		self.hitrost_y = -1

	def move(self):
		self.x += self.hitrost_x
		self.y += self.hitrost_y

class Svet:
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.plosca = Plosca(x=width // 3, y=height - 2, sirina=6)
		self.zoga = Zoga(x=width // 2, y=height // 2)

	def move(self, i: int):
		if i % 5 == 0:
			self.zoga.move()

			if self.plosca.x <= self.zoga.x <= self.plosca.x + self.plosca.sirina and self.zoga.y == self.plosca.y:
				self.zoga.hitrost_y *= -1

			if self.zoga.x < 0:
				self.zoga.hitrost_x *= -1
				self.zoga.x = 0

			if self.zoga.x > self.width-1:
				self.zoga.hitrost_x *= -1
				self.zoga.x = self.width-2

			if self.zoga.y < 0:
				self.zoga.hitrost_y *= -1
				self.zoga.y = 0

			if self.zoga.y > self.height-1:
				self.zoga.hitrost_y *= -1
				self.zoga.y = self.height-2
				return False

		return True
