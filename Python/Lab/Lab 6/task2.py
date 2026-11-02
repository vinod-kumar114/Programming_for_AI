import numpy as np
np.random.seed(42)
ai = np.random.uniform(10,100,size=(10,4))
# print(ai)

avg = np.mean(ai, axis=0)
st = np.std(ai, axis=0)

print(avg)
print(st)

ai_standarize = (ai-avg)/st

n_avg = np.mean(ai_standarize, axis=0)
n_st = np.std(ai_standarize, axis=0)
print(n_avg)
print(n_st)