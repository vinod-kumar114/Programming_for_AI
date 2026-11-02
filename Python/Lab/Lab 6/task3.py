import numpy as np

img = np.random.randint(0,255,size=(8,8))
min_int = np.min(img)
max_int = np.max(img)
mean_int = np.mean(img)

threshold = 100
mask = img>threshold

t_img = np.where(img>threshold, 1,0)

print(t_img)