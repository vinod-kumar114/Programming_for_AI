import numpy as np

sensor_data = np.random.normal(loc=25, scale=5, size=(5, 10))

# sensor_means = np.mean(sensor_data, axis=1)
# sensor_mins = np.min(sensor_data, axis=1)
# sensor_maxs = np.max(sensor_data, axis=1)
# sensor_stds = np.std(sensor_data, axis=1)

# highest_sensor_idx = np.argmax(sensor_means)

# cutoff = 30.0
# above_threshold = sensor_data > cutoff

# print("Per-sensor Mean:", sensor_means)
# print("Per-sensor Min:", sensor_mins)
# print("Per-sensor Max:", sensor_maxs)
# print("Per-sensor Std:", sensor_stds)
# print("Sensor with highest average reading:", highest_sensor_idx)
# print("Readings above threshold:\n", above_threshold)

