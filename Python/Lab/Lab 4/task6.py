"""6. You are developing a Smart Computer Resource Manager that monitors the resources of a computer and automatically determines whether the system is operating normally or requires attention.Design and implement a Python class named Computer.
 The class should store: [CPU usage ,  RAM usage, Battery level]
 Create a method named: system_status()
 The method should analyze the resource values and generate appropriate warnings.
 Use the following conditions:
Condition Warning
CPU > 80% Heavy CPU Load
RAM > 85% High Memory 
Usage
Battery <  Low Battery
 Create at least two computer objects with different resource values.
CONSTRAINTS : If more than one condition is true, the program should display all applicable warnings.
For example, if CPU is 90% and battery is 15%, the program should report both:
Heavy CPU Load
Low Battery"""



class Computer:
    def __init__(self,cpu_usage,ram_usage,battery_level):
        self.cpu_usage=cpu_usage
        self.ram_usage=ram_usage
        self.battery_level=battery_level

    def system_status(self):
        print("\nThe system has: ")
        if self.cpu_usage >80:
            print("\tHeavy CPU Load", self.cpu_usage)

        if self.ram_usage >85:
            print("\tHigh Memory Usage",self.ram_usage)

        if self.battery_level <20:
            print("\tLow Battery", self.battery_level)


comp1 = Computer(cpu_usage=90,ram_usage=70,battery_level=15)
comp2 = Computer(cpu_usage=50,ram_usage=90,battery_level=80)

comp1.system_status()
comp2.system_status()