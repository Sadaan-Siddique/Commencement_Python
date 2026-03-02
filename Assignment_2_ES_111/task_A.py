import numpy as np

rng = np.random.default_rng()

floatVal = rng.random()
# 1. Single float between 0 and 1
print("Random float (1 to 2):",round(floatVal + 1, 4)) 

# 2. Array of 5 floats between 0 and 1
floatArr = rng.random(5) # will generate a numpy.ndarray of 5 floats ranging from [1,2)
print("Array of 5 Random Floats:",floatArr)

# 3. 5 Random integers between 1 and 50
print(rng.integers(1, 50, 5))