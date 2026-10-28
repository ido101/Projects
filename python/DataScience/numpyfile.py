import numpy as np

# np_2d = np.array([[2, 5, 2, 3], [5, 5, 3, 2]])
# print(np_2d)
# print(np_2d[1, 1])
# generate a 5x5 random array and round it up to two digits after the decimal point
height = np.round(np.random.normal(1.75, 0.20, (5, 5)), 2)
print(height)
# print the first row
print(height[0, :])
# print the first column
print(height[:, 0])
# print the length of the first row
print(len(height[0]))
# print the average of all the numbers in the first row
print(np.mean(height[0]))
# print the middle value
print(np.median(height[0]))
