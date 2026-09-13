"""A cybersecurity company is developing a system that uses different security tools to respond to cyber attacks. Although every security tool performs a different action, all of them should provide a common respond() method. Design this system using inheritance and polymorphism.
 Create a parent class named: SecuritySystem , with a method: respond()
 Create the following child classes:[ Firewall, Antivirus, IntrusionDetectionSystem]
 Each child class must override the respond() method.
 Their responses should be different. For example:
o Firewall → Block suspicious network traffic
o Antivirus → Isolate malicious files
o ntrusion Detection System → Generate security alert"""






class SecuritySystem():
    def respond(self):
        pass

class Firewall(SecuritySystem):
    def respond(self):
        print("Block suspicious network issue.")


class Antivirus(SecuritySystem):
    def respond(self):
        print("Isolate malicious files.")


class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Generate security alert")


c1 = [Firewall(), Antivirus(), IntrusionDetectionSystem()]
for classes in c1:
    classes.respond()

