import numpy as np


arr = np.array([1,np.nan,3,4,np.nan,7, np.nan])

print(np.isnan(arr))
print(np.nanmean(arr))
print(np.nansum(arr))
print(np.nanstd(arr))

arr[np.isnan(arr)] = np.nanmean(arr)

print(np.isnan(arr).any())