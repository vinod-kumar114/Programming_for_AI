import numpy as np

rng1 = np.random.default_rng(seed=123)
data1 = rng1.normal(loc=0, scale=1, size=1000)

mean1 = np.mean(data1)
median1 = np.median(data1)
std1 = np.std(data1)
min1 = np.min(data1)
max1 = np.max(data1)
within_1std_1 = np.mean((data1 >= (mean1 - std1)) & (data1 <= (mean1 + std1))) * 100

print("--- Seed 123 ---")
print("Mean:", mean1)
print("Median:", median1)
print("Std:", std1)
print("Min:", min1)
print("Max:", max1)
print("Percentage within 1 std:", within_1std_1, "%")

rng2 = np.random.default_rng(seed=456)
data2 = rng2.normal(loc=0, scale=1, size=1000)

mean2 = np.mean(data2)
median2 = np.median(data2)
std2 = np.std(data2)
min2 = np.min(data2)
max2 = np.max(data2)
within_1std_2 = np.mean((data2 >= (mean2 - std2)) & (data2 <= (mean2 + std2))) * 100

print("\n--- Seed 456 ---")
print("Mean:", mean2)
print("Median:", median2)
print("Std:", std2)
print("Min:", min2)
print("Max:", max2)
print("Percentage within 1 std:", within_1std_2, "%")