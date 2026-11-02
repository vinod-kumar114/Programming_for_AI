class SecurityTool:
    def respond(self):
        print("Generic Security Response.")

class Firewall(SecurityTool):
    def respond(self):
        print("Blocking suspicious network traffic")

class Antivirus(SecurityTool):
    def respond(self):
        print("Isolating malicious files")

res = [Antivirus(), Firewall()] # paranthesis lagany se object banty hen

for i in res:
    i.respond()