
# "Self" = keyword "this"
class my_Drones:
	def __init__(self, color = "color", fc = "fc", name = "name"):
		self.__color = color
		self.__fc = fc
		self.__name = name
		
	def get_color(self):
		return self.__color
		
	def set_color(self, color):
		self.__color = color
		
	def get_fc(self):
		return self.__color
		
	def set_fc(self, fc):
		self.__fc = fc
		
	def get_name(self):
		return self.__name
		
	def set_name(self, name):
		self.__name = name
	
	
drone1 = my_Drones()
drone1.set_color("Silver")
drone1.set_fc("Betaflight")
drone1.set_name("Acrobee")

	
print("This drone is " + drone1.get_color() + "\n" +
	  "The flight controller is: " + drone1.get_fc() + "\n"
	  "The model name is: " + drone1.get_name() + "\n")

