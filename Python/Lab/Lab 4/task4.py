"""You are designing a control system for different types of autonomous robots. Each robot performs a different type of movement, but all robots share common properties such as name and battery level.Design and implement this system using OOP.
 Create a parent class named:Robot
 The class should contain:[ name, battery]
 Create the following methods:[ move(), charge()]
 Create three child classes:
o DeliveryRobot
o SecurityRobot
o RescueRobot
 Each child class should provide its own implementation of the move() method.
o Delivery Robot → moves to a delivery location
o Security Robot → patrols a specific area
o Rescue Robot → moves toward a disaster location
Constraint : A robot should not be allowed to move when its battery level is below 20%"""



class Robot():
    def __init__ (self,name,battery):
        self.name=name
        self.battery=battery

    def move(self):
        pass

    def charge(self):
        print("The robot is being charged.")

class DeliveryRobot(Robot):
    def move(self):
        if self.battery<20:
            print(self.name,"can't move, cuz low battery.")
        else:
            print(self.name,"is moving to the delivery location.")


class SecurityRobot(Robot):
    def move(self):
        if self.battery<20:
            print(self.name,"can't move, cuz low battery.")
        else:
            print(self.name,"is patrolling an area.")


class RescueRobot(Robot):
    def move(self):
        if self.battery<20:
            print(self.name,"can't move, cuz low battery.")
        else:
            print(self.name,"is moving towards a disaster location.")



robo1 = DeliveryRobot("Daraz_Robot",98)
robo2 = SecurityRobot("Cyber_Robot", 50)
robo3 = RescueRobot("Fighter",13)

robo1.move()
robo2.move()
robo3.move()
