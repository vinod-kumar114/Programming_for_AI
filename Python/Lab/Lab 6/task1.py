import numpy as np

set1 = np.arange(80, 100, 2)
set2 = np.arange(50, 80, 1)
set3 = np.arange(30, 50, 2)
set_arr = np.concatenate([set1, set2, set3])
np.random.shuffle(set_arr)
dataset = set_arr.reshape(10, 5)

st_total = np.sum(dataset, axis=1)
print("Student totals: ",st_total)

st_avg = np.mean(dataset, axis=1)
print("Student average: ", st_avg)

sub_avg = np.mean(dataset, axis=0)
print("Subject avg: ", sub_avg)

st_high_avg = np.argmax(st_avg)
print("Student with highest avg: ", st_high_avg)

c=np.sum(st_avg>=50)
print("Count of students with avg >= 50: ", c)

print(np.where(st_avg>=50,"Pass","Fail"))
