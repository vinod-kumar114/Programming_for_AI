import numpy as np

np.random.seed(42)

image = np.random.randint(0,255, size=(8,8))
# print(image)

mean_int = np.mean(image)
min_int = np.min(image)
max_int = np.max(image)

print("Minimum intensity:",min_int, "\nMaximum Intensity:",max_int,"\nMean Intensity:",mean_int )

threshold = 80
print(np.where(image>threshold, 1, 0))