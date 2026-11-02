import numpy as np

arr = np.array([10.0, 20.0, np.nan, 40.0, np.nan, 60.0, 70.0])

nan_mask = np.isnan(arr)

nan_mean = np.nanmean(arr)
nan_sum = np.nansum(arr)
nan_std = np.nanstd(arr)

arr[np.isnan(arr)] = nan_mean

has_nan = np.isnan(arr).any()

print("NaN Mask:", nan_mask)
print("NaN Mean:", nan_mean)
print("NaN Sum:", nan_sum)
print("NaN Std:", nan_std)
print("Cleaned Array:", arr)
print("Any NaNs left?:", has_nan)