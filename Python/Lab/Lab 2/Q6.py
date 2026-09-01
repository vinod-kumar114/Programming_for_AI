"""6.A server generates thousands of log entries containing information such as:
INFO, ERROR, WARNING, INFO , ERROR, INFO
Develop a program that analyzes the logs and determines:
 How many times each log type occurred
 Which log types appeared
 The most frequently occurring log type
Requirement: The solution should work efficiently as the number of log entries increases."""


lis = ["INFO", "ERROR", "WARNING", "INFO" , "ERROR", "INFO"]

dic = {}
for log in lis:
    if log in dic.keys():
        dic[log]+=1
    else:
        dic[log] = 1
print(dic)


uniqueLogs = set(dic.keys())



freqLog = ""
highest =0
for i, j in dic.items():
    if j>highest:
        highest=j
        freqLog=i
print(highest, freqLog)