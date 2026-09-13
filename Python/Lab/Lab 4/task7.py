""" You are working as a software developer for a cybersecurity company. The company wants to develop a prototype of an Autonomous Cyber Defense System.The system contains multiple intelligent cyber agents. Each agent analyzes security events and performs an appropriate response.Design and implement this system using OOP principles.
 Create a parent class named: CyberAgent
 The class should contain: [Agent name, Status, A private threat score]
 Implement appropriate methods to update and retrieve the threat score.
 Create the following child classes:
o NetworkAgent
o MalwareAgent
o IncidentResponseAgent
 Each child class should implement its own versions of: analyze() ,respond()"""

class CyberAgent():
    def __init__(self,agentName,status,threatScore):
        self.agentName=agentName
        self.status=status
        self.__threatScore=threatScore

    def update_threatScore(self,newScore):
        self.__threatScore=newScore
        print("Threat score updated scuccessfully.")

    def get_threatScore(self):
        return self.__threatScore

    def analyze(self):
        pass

    def respond(self):
        pass

class NetworkAgent(CyberAgent):
    def analyze(self):
        print("The network agent is analyzing the network threat. The threat sccore is",self.get_threatScore())

    def respond(self):
        print("The network threat is undercontrol.")

class MalwareAgent(CyberAgent):
    def analyze(self):
        print("The malware agent is analyzing the malware threat. The threat sccore is",self.get_threatScore())

    def respond(self):
        print("The malware threat is undercontrol.")

class IncidentResponseAgent(CyberAgent):
    def analyze(self):
        print("The incident responce agent is analyzing the incident situation and threat. The threat sccore is",self.get_threatScore())

    def respond(self):
        print("The situation threat is undercontrol.")


agents = [NetworkAgent("NetVerse","active", 55), MalwareAgent("MalwareWorld","non-active", 0), IncidentResponseAgent("Golu", "active", 62)]

for agent in agents:
    agent.respond()

for agent in agents:
    agent.analyze()
