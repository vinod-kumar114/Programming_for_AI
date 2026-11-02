import numpy as np

np.random.seed(42)
sensors = np.random.uniform(20.0,100.0, size=(5,6))
print(np.round(sensors,3))