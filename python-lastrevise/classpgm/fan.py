class Fan:
    SLOW=1
    MEDIUM=2
    FAST=3
    def __init__(self,speed=SLOW,radius=5,color="blue",on=False):
        self.__speed=speed
        self.__radius=radius
        self.__color=color
        self.__on=on
    
    def get_speed(self):
        return self.__speed
    def get_radius(self):
        return self.__radius
    def get_color(self):
        return self.__color
    def get_on(self):
        return self.__on

    def set_speed(self,speed):
        self.__speed=speed
    def set_radius(self,radius):
        self.__radius=radius
    def set_color(self,color):
        self.__color=color
    def set_on(self,on):
        self.__on=on
        
f1=Fan()
f1.set_speed(Fan.FAST)
f1.set_radius(10)
f1.set_color("Yellow")
f1.set_on(True)
print("Properties: ")
print(f"Speed {f1.get_speed()}")
print(f"Color {f1.get_color()}")
print(f"Radius {f1.get_radius()}")
print(f"ON {f1.get_on()}")