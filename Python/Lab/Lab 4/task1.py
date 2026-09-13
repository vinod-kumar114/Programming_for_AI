"""You are developing a basic Cybersecurity Threat Detection System for a computer network. The system monitors 
different devices and determines their security status based on the detected threat level.Design and implement a 
Python class named ThreatDetector.
 The class should contain the following attributes (device_name, ip_address, threat_level).
 Create a method named scan() that displays the security status of the device.
 The system should classify the device according to the following rules:
    Threat Level                 System Response
       Low                          System Safe
       Medium                       Suspicious Activity
       High                         Critical Threat Detecte"""


class ThreatDetector():
    def __init__ (self, device_name, ip_address, threat_level):
        self.device_name=device_name
        self.ip_address=ip_address
        self.threat_level=threat_level

    def scan(self):
        if self.threat_level == "low" or self.threat_level =="Low":
            print("System Safe.")
        elif self.threat_level == "medium" or self.threat_level =="Medium":
            print("Suspicious Activity.")
        elif self.threat_level == "high" or self.threat_level =="High":
            print("Critical threat detected.")

d1 = ThreatDetector("mobile",1982,"low")
d1.scan()