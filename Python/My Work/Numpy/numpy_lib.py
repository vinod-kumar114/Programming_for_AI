# Importing numpy library
import numpy as np

# check version
# print(np.__version__)


# ============== START ==============

# creating 1D array
arr_1d = np.array([1,2,3,4,5,6,7])
# print(arr_1d)
# print(arr_1d*2) # 2 will multiply with all elements



# 2D array: matrix
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) # it is 3x3 matrix, 3 rows and each row contains 3 columns
arr_2d_2 = np.array([[1,2],[3,4],[4,5],[6,7],[8,9]]) # 5x2 matrix, 5 rows and each row 2 cols
# print(arr_2d)
# print(arr_2d_2)
# 2D contains multiple 1D arrays

# 3D array
arr_3d = np.array([[[1,2],[2,3]],[[3,4],[4,5]],[[5,6],[6,7]]]) 
# print(arr_3d)
# 3D contains multiple 2D arrays


# The logic here is simple: jitni dimension ki array chahiye utni braces add kro []. Aur usme, dim-1 ki arrays put kro


# ===== Array of 0s and 1s =======

zero_1d = np.zeros(5, dtype=int) # 1D of zeros
zero_2d = np.zeros((2,3), dtype=int) # note: must add ( ) for 2d --- dtype shows which type we want, int or float
zero_3d = np.zeros((2,3,4), dtype=int) # formula ((depth, rows, cols)) : depth means ke kitny 2d arrays hongy isme
# print(zero_1d)
# print(zero_2d)
# print(zero_3d)

# the same thing goes for array of ones 1s, just apply np.ones() at the place of np.zeros


# ========== Full, Emepty, and Identity arrays =======

# np.full() --- creates an array of elements we specify
# np.empty() --- might put dummy values
# np.eye() --- creates identity matrix

f = np.full((2,3,4), 5) # --- create a 3x4 matrix, containing 7 at all places
# print(f)
emp = np.empty((3,3)) # --- creating a 3x3 empty arra, we will get dummy values
# print(emp)
I = np.eye(4) # --- creating a 3x3 identity matrix. Note: we can't assign dimensions. we can only give one element like 2,3,4 -- it will itself make 2x2, 3x3, 4x4. No 3D or 4D possible
# print(I)


# =========== arange() -> array in range===== 

# puts numbers in a specified range : np.arange(start, stop, steps) -> same as range
arr_range = np.arange(0,11,2) # 0-10, even nums: we can also write it as np.arange(11) --- it will print from 0-10, with no steps
# print(arr_range)

# we can create any type of array with arange, but we have to make use of 'reshape()' function
arr_range_reshaped = arr_range.reshape(2,3)
# print(arr_range_reshaped)


# ========== np.linspace(start, stop, num) =================

a = np.linspace(1,12,20, dtype=int) # --- we don't provide steps here. it will give us the numbers in the provided numbers. We will give it starting pos, ending pos, and num -> how many nums we want in that range; here start=1, end=12, we need 20 nums
# print(a) 
# again we can use reshape to give it a shape


# ============== ARRAY ATTRIBUTES ============
# array attributes give us info about the array without effecting it

arr = np.array([[10,20,30],[40,50,60]], dtype=np.int32)

# print(arr.ndim) # --- ndim: no. of dimensions
# print(arr.size) # --- size: no. of elements in array
# print(arr.dtype) # --- dtype: type of array -- int, float
# print(arr.itemsize) # --- itemsize: size of the element in byte
# print(arr.nbytes) # --- nbytes: total no. of bytes in array 
# print(arr.shape) # --- shape: size along with dimension
#   - shape plays a key role. If our array is 2D of 2x3, it will print -- (2,3): 2 rows, 3 cols; But if array is 3D, and it has 2 2D arrays in it, then it will print: (2,2,3) -- 2 2D arrays, 2 r, 3 c. The rightmost num will tell us the no of arrays in in the leading dimension array;  three num in 3D, 4 num in 4D ....



# ============= numpy data types (dtype) =============

# dtype=np.int32, dtype=np.float64, dtype=bool
# boolll = np.array([True, True, False], dtype=bool)

#  ====== Type Conversion ===== use: stype(np.__)
# type_arr = np.array([1.2, 2.8, 3.9])
# integers = type_arr.astype(np.int32)
# print(integers)



# ================== INDEXING =============
# accessing specific element in array

# 1D is same as list
ind_1d = np.array([10,20,30,40,50])
# print(ind_1d[0]) # --> first element
# print(ind_1d[1])
# print(ind_1d[-1]) # --> last element

# 2D 
ind_2d = np.array([
    [10,20,30],
    [40,50,60],
    [70, 80, 90],
])
#  print(ind_2d[row, col]) row: row no., col: col no.
# print(ind_2d[1,2]) # --> 2nd row, 3rd col --> 60

# for entire row: [row, :] ---- for entire col: [:, col]
# print(ind_2d[2, :]) # -- 3rd row
# print(ind_2d[:, 0]) # -- 1st col


# 3D
ind_3d = np.array([
    [[1, 2], [3, 4]],   # Layer 0
    [[5, 6], [7, 8]]    # Layer 1
])
# Layer 1 ke andar, Row 0, Column 1 wala element:
# print(ind_3d[1,0,1]) # -- 6
# print(ind_3d[0,1,1]) # -- 4



#  ============= Chaging Values ================
# Note: with the help of indexing we can change the values of elements in the array or matrix
# ind_3d[1,0,1] = 7



# ================== SLICING & Reshaping =============
# select a range of elements

# 1D
slc_1d = np.array([10, 20, 30, 40, 50, 60])
# print(slc_1d[1:5]) # 2nd element to 5th element: 20-50
# print(slc_1d[:3]) # 10, 20, 30
# print(slc_1d[3:]) # 40, 50, 60
# print(slc_1d[::2]) # all elements with 2 steps: 10,30,50

# 2D
# array[row_slice, col_slice]
slc_2d = np.array([
    [10, 20, 30, 40],   # Row 0
    [50, 60, 70, 80],   # Row 1
    [90, 100, 110, 120] # Row 2
])
# print(slc_2d[0:2,1:3]) # -- rows 0-2: r0 and r2. cols 1-3: c1 and c2 
# print(slc_2d[:2, :3])
# [[20,30],1:
#  [60,70]]


# ================== RESHAPING -- arr.reshape()  =============    
# reshape changes the shape of array

resh_arr = np.arange(1, 13)
matrix = resh_arr.reshape(3, 4)
# print(matrix)
# print(matrix.shape)

# reshape( , -1)
# -1 here lets numpy choose dimension automatically
mat2 = resh_arr.reshape(4,-1)
# print(mat2)

#  ---- Flatten & Ravel ----
# Both flatten() and ravel() convert a multidimensional array into 1-D. 
# flatten() normally creates a separate copy of the data.
# ravel() generally returns a view when possible, so changes can affect the original array.
fr_arr = np.array([[1, 2], [3, 4]])
# print(fr_arr.flatten())
# print(fr_arr.ravel())
# print(fr_arr)



# ================== Transpose  ============= 
# You can use arr.T or np.transpose(arr) -- same same
# print(fr_arr)
# print(fr_arr.T)
# print(np.transpose(fr_arr))


# ================== Concatenate  ============= 
# Concatenate: joins arrays together, the order should be same
a = np.zeros((3,4))
b = np.ones((3,4))
# print(np.concatenate((a,b)))
# it will concatenate vertically, will first print a, and then b vertically. but we can concatenate it horizontally as well. using 'axis' if axis=0 (default), it will be vertically, if axis is 1, it will be horizontally
# print(np.concatenate((a,b),axis=1))


# ================== Splitting arrays  ============= 
# opposite of combining arrays;
# np.split( , )

sp_arr = np.arange(12)
# print(np.split(sp_arr,3)) # --- array1[0,1,2,3], array2[4,5,6,7], array3[8,9,10,11] . These are splitted in this way. 3 shows that we want to split it in 3 arrays

# we can split horizontally and vertically as well
# print(np.hsplit(sp_arr,3)) #-- default
mat = np.arange(24).reshape(6,4)
# print(mat)
# print(np.vsplit(mat,2)) # it works on array of 2 or more dimensions


# ================== Array Arithmetic  ============= 
#  only possible when dimensions are same

a = np.array([1, 2, 3, 4], dtype=np.int32)
b = np.array([10, 20, 30, 40], dtype=np.int32)
# print(a+b)
# print(b-a)
# print(a@b)
# print(b/a)
# print(b**2)
# print(b%3)


# -------------- Instead we can use: UNIVERSAL FUNCTIONS ---------
# print(np.add(a,b))
# print(np.subtract(b,a))
# print(np.multiply(a,b))
# print(np.divide(b,a))
# print(np.power(a,2))
# print(np.sqrt(b))
# we can find: square(), sin(), log(), exp() ...



# ================== AGGREGATION FUNCTIONS ============= 
# np.sum(), mean, median, min, max, std, var, argmin, argmax, prod ...


# ================= Axis in numpy ===================
# axis parameter controls the direction along which the operation is performed. for 2D, axis=0 -> row wise, vertical directoin, axis=1 -> col wise, horizontal direction
marks = np.array([[70, 80, 90],
                  [60, 75, 85],
                  [90, 95, 88]
])
# print(np.sum((marks), axis=0)) # all rows added to a single row
# print(np.sum((marks), axis=1)) # ll cols added to a single col


# ================= Comparison and Boolean Arrays =================
# it compares each element of array with the provided value and gives answer in True of False
arrayy = np.arange(10,110,10).reshape(2,5)
# print(arrayy>60)
# print(arrayy[0,3]==40) # -- at index row 0, col 3 -> 40 
#  if we want numbers greater than 50:
# print(arrayy[arrayy>50]) # -- it will only print numbers that are greater than 50; wont give true flase now

# we can use it in many different ways, just think and try..


# ===== np.where() -- instead of true false, we print our own values
# it works like if else: np.where(condition, if true: "Yes", else "No" )
arrayy = np.arange(10,110,10)
# print(np.where(arrayy>=50, "Yes", "No"))


# ================= Broadcasting =================
# to perfrom operations among different shapes of arrays
# a single element can be performed with any kinda array. 1D array will work with all rows 

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
# print(arr + 10)
# row = np.array([10, 20, 30])
# print(arr + row)



# ================= Random Numbers =================
# we use rng = np.random.default_rng(42) --- 42 is a seed value, it will make sure that we will always get same values during the current time

rng = np.random.default_rng(42)
# print(rng.random(5)) # --- 1D array of 5 random nums
# print(rng.random((3,4))) # --- 3x4 2d array of random nums

# random integers: rng.integers(low, high, size) --- high is not included
# print(rng.integers(1,11, size=5)) # --- 5 number ki 1D array, size-> output shape
# print(rng.integers(1,13, size=(3,4))) # --- 12 nums ki 3x4 2D array

# --------------========~~~~~~~~~~~~~~~~~~~~============-----------
# gaussian / normal distribution ke hissab se random num generate krta hy : rng.normal()

# --- Real-world real life data (jaise logo ki height, exam marks, blood pressure, sensor noise, ML models ke starting weights) lagbhag hamesha Normal Distribution follow karte hain. Isiliye Machine Learning aur Data Science mein rng.normal() sab se zyada use hone wala random function hai.

# rng.normal(loc = mean(avg), scale= standard deviation, size=output shape)
# print(rng.normal(loc=0, scale=1, size=5))




# ================= Sorting and Searching =================
# np.sort() sorts the actual values of an array.
# np.argsort() returns the indexes that would produce the sorted order.
# np.argmax() and np.argwhere() help locate specific values or conditions.
arr = np.array([50, 10, 40, 20, 30])
# print(np.sort(arr))
# print(np.argsort(arr))
# print(np.argmax(arr))
# print(np.argwhere(arr > 25))



# ================= Unique Values =================
# numpy m unique values and unki freq find krny ke liye 
# np.unique(arr) use hota hy
arr = np.array([1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4])
# print(np.unique(arr))

# unique value and count nikalny ke liye unique() ke andr return_counts=True add kro
values, counts = np.unique(arr, return_counts=True)
# for val, cnt in zip(values, counts):
#     print(val,":" ,cnt)


# ================= Copying in numpy=================
# 2 ways: 
# 1. view: A view shares the same underlying data with the original array.
original = np.array([10, 20, 30, 40])
v = original.view()
# print(original,v)
# v[3]=5
# print(original,v)

# A copy creates independent data, so modifying it does not affect the original.

deep_copy = original.copy()
# print(original,deep_copy)
# deep_copy[3]=5
# print(original,deep_copy) # -- no change in original array


# ================= Inserting, Deleting, Appending ================
arr = np.array([1, 2, 3])
# print(np.append(arr, 4))
# print(np.insert(arr, 1, 99))
# print(np.delete(arr,2)) # -- here 2 points the index


rng = np.random.default_rng(42)
arr = rng.integers(1,100, (10,10))

print(arr)

# dataset = np.random.randint(30, 100, size=(10,5))
# # print(dataset)

# total = np.sum(dataset, axis=1)
# print(total)

# avg = np.mean(dataset, axis=1)
# print(avg)

