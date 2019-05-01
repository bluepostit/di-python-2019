class Car:
	def __init__(self, color, model):
		self.color = color
		self.model = model

	def __str__(self):
		return "A {} {} car".format(
			self.color, self.model)


def test():
	c = Car('black', '2020')
	d = Car('blue', '2011')
	print("Cars: {}, {}".format(str(c), str(d)))

	if c > d:
		print("c is greater")

test()