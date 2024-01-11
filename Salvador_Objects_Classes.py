import math


class Circle:
	def __init__(self, radius):
		self.radius = radius
		self.pi = math.pi

	def area(self):
		return round(self.pi * self.radius ** 2, 2)


	def perimeter(self):
		return round(2 * self.pi * self.radius, 2)


while True:
	try:
		radius_in = int(input("Radius: "))
		if radius_in <= 0:
			print("Please enter a valid value.")
		else:
			square = Circle(radius=radius_in)
			break
	except ValueError:
		print("Enter a valid value.")

print("Area:",square.area())
print("Perimeter:",square.perimeter())