import numpy as np

np.random.seed(42)
# print(np.__version__)
dataset = np.random.randint(20,100, size=(10,5))
# print(dataset)

std_total = np.sum(dataset, axis=1)
print("Student total: ",std_total)

std_avg = np.mean(dataset, axis=1)
print("Student average: ",std_avg)

sub_avg = np.mean(dataset, axis=0)
print("Subject average: ",sub_avg)

std_high_avg = np.argmax(std_avg)
print("Student with highest overall average: ",std_high_avg)

count = np.sum(std_avg>=50)
print("No of students having average at least 50: ",count)

print(np.where(std_avg>=50, "Pass", "Fail"))