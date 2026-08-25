strin = input("Enter the string: ")
reve = ""
for i in range(len(strin)-1, -1, -1):
    reve+=strin[i]
print(reve)