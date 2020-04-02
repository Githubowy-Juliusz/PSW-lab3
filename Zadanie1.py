class RGB:
	def __init__(self, R_value, G_value, B_value):
		self.set_R_value(R_value)
		self.set_G_value(G_value)
		self.set_B_value(B_value)
	def get_R_value(self):
		return self.R_value
	def get_G_value(self):
		return self.G_value
	def get_B_value(self):
		return self.B_value
	def __check_type_and_value(self, value):
		if not isinstance(value, int):
			raise TypeError("NOT AN INTEGER")
		if not (value >= 0 and value <= 255):
			raise ValueError("VALUE HAS TO BE BETWEEN 0 AND 255")
	def set_R_value(self, value):
		self.__check_type_and_value(value)
		self.R_value = value
	def set_G_value(self, value):
		self.__check_type_and_value(value)
		self.G_value = value
	def set_B_value(self, value):
		self.__check_type_and_value(value)
		self.B_value = value
	def __str__(self):
		r = str(self.get_R_value()) + ", "
		g = str(self.get_G_value()) + ", "
		b = str(self.get_B_value()) + "]"
		return "[" + r + g + b

class RGBController:
	def __check_type(self, colour):
		if not isinstance(colour, RGB):
			raise TypeError("NOT RGB")
	def initialize_colour(self, colour, red, green, blue):
		self.__check_type(colour)
		colour.set_R_value(red)
		colour.set_G_value(green)
		colour.set_B_value(blue)
	def print_colour(self, colour):
		self.__check_type(colour)
		print(colour)
	def mix_colours(self, colour1, colour2):
		self.__check_type(colour1)
		self.__check_type(colour2)
		mixed_r = int((colour1.get_R_value() + colour2.get_R_value()) / 2)
		mixed_g = int((colour1.get_G_value() + colour2.get_G_value()) / 2)
		mixed_b = int((colour1.get_B_value() + colour2.get_B_value()) / 2)
		return RGB(mixed_r, mixed_g, mixed_b)

def test():
	controller = RGBController()
	colour1 = RGB(0, 255, 255)
	colour2 = RGB(125, 0, 0)
	colour3 = controller.mix_colours(colour1, colour2)
	controller.print_colour(colour1)
	controller.print_colour(colour2)
	controller.print_colour(colour3)
	controller.initialize_colour(colour2, 0, 125, 125)
	print(colour1.get_R_value())
	print(colour2.get_G_value())
	print(colour3.get_B_value())
	colour1.set_R_value(15)
	colour2.set_G_value(15)
	colour3.set_B_value(15)
	controller.print_colour(colour1)
	controller.print_colour(colour2)
	controller.print_colour(colour3)
test()
