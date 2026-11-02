class Robot:
    def __init__(self, name, battery=100):
        self.name = name
        self.__battery = battery

    def get_battery(self):
        return self.__battery

    def move(self):
        print("Robot is moving")

class RescueRobot(Robot):
    def __init__ (self, name):
        super().__init__(name)

    def move(self):
        if self.get_battery() >=20:
            print("RescueRobot moving to disaster site 🚨")
        else:
            print("Low battery! Cannot move")
    