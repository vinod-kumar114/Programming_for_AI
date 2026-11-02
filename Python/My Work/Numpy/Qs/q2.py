"""
2. Create a 10×4 numerical feature matrix representing four input features for an AI model. Calculate the mean and standard deviation of every feature and standardize each feature using vectorized operations. Verify that the resulting feature means are approximately zero and standard deviations are approximately one. Explain how broadcasting is used.
"""

"""
Feature Standardization (Z-score Scaling):
    In ML, when we have data of different ranges, then we do this step to take all the data ranges the same scale.
    (Machine learning mein jab humare paas alag-alag range ka data hota hai, toh hum usko ek hi paimane (scale) par laane ke liye ye step karte hain.)

    Step 3: Standardization Formula:
                        matrix_standardized = (matrix - mean) / std

    
    Step 4: Verification (Tasdeeq):
    Jab koi data standardize ho jata hai, toh:Uska Naya Mean approx 0 ho jata hai.Uska Naya Standard Deviation approx 1 ho jata hai.
"""

"""
Broadcasting Kya Hai? (Aasan Misaal)
Is question ka sabse important hissa Broadcasting hai.
    - matrix ka size hai: (10, 4) (10 rows, 4 columns)
    - mean ka size hai: (4,) (sirf 4 values)

Jab aap matrix - mean likhte hain, toh Python automatic samajh jata hai ke:
    - mean ki pehli value ko matrix ke pehle column ki tamaam 10 values se minus karna hai.
    - mean ki doosri value ko doosre column ki 10 values se minus karna hai... aur isi tarah aage.

Python ne background mein us 4 values wali line ko 10 dafa repeat karke (10, 4) ke barabar bana diya taake minus ho sake. Isi automatic size barabar karne ke process ko Broadcasting kehte hain!
"""







import numpy as np

np.random.seed(42)
matrix = np.random.randint(10,100, size=(10,4))

avg = np.mean(matrix, axis=0)
std = np.std(matrix, axis=0)

print("Average: ", avg, "\nStandard Deviation: ", std)

standarized = (matrix - avg)/std

stz_avg = np.mean(standarized, axis=0)
stz_std = np.std(standarized, axis=0)

print("New Average: ", np.round(stz_avg,5), "\nNew Standard Deviation: ", np.round(stz_std,5))



import numpy as np

# 1. Create a 10x4 numerical feature matrix (10 samples, 4 features)
# Using a fixed seed for reproducible random values
np.random.seed(42)
X = np.random.randint(10, 100, size=(10, 4))
print("Original Feature Matrix (X):\n", X)

# 2. Calculate mean and standard deviation for each feature (column-wise)
# axis=0 performs the aggregation vertically down each column (across rows/samples)
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

print("\nMean of each feature (axis=0):\n", mean)
print("Standard Deviation of each feature (axis=0):\n", std)

# 3. Standardize each feature using vectorized operations: Z = (X - mean) / std
X_standardized = (X - mean) / std
print("\nStandardized Feature Matrix (X_standardized):\n", X_standardized)

# 4. Verify that resulting means are approximately 0 and standard deviations are 1
new_mean = np.mean(X_standardized, axis=0)
new_std = np.std(X_standardized, axis=0)

print("\n--- Verification ---")
print("New Means (should be ~0):\n", np.round(new_mean, 5))
print("New Standard Deviations (should be ~1):\n", np.round(new_std, 5))