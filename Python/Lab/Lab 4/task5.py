"""You are developing a simple AI Agent System in which different intelligent agents perform different tasks. Although the agents have different responsibilities, the system should interact with all agents through a common method called perform_task().
 Create a parent class named:Agent 
 with the following attributes: [name , status]
 with following method:perform_task()
 Create three child classes:
1. SecurityAgent
2. MonitoringAgent
3. RecoveryAgent
 Each child class should override perform_task() and perform a different task.
1. SecurityAgent → Detecting cyber threat
2. MonitoringAgent → Monitoring system activity
3. RecoveryAgent → Recovering system services"""


class Agent():
    def __init__(self,name,status):
        self.name=name
        self.status=status

    def perform_task(self):
        pass


class SecurityAgent(Agent):
    def perform_task(self):
        if self.status=="Active" or self.status=="active":  
            print(self.name,"is detecing Cyber threat")
        else:
            print("The agent is not active.")


class MonitoringAgent(Agent):
    def perform_task(self):
        if self.status=="Active" or self.status=="active":
            print(self.name,"is monitoring system activity")
        else:
            print("The agent is not active.")


class RecoveryAgent(Agent):
    def perform_task(self):
        if self.status=="Active" or self.status=="active":
            print(self.name,"is recovering system services")
        else:
            print("The agent is not active.")


agent = [SecurityAgent("Claude","Active"), MonitoringAgent("Gemini","Active"), RecoveryAgent("ChatGPT","not")]

for a in agent:
    a.perform_task()