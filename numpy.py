# Python Numpy
# One Dimensional Array 
import numpy as nd
my_array = nd.array([1,10,20,40,50,45,34])
print(my_array)
print(type(my_array))
print(my_array[6])
print(my_array.dtype)
my_array [3] = 400
print(my_array)
print(my_array[1:4])
# Two Dimensional Array
import numpy as nd
my_array = nd.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(my_array)
print(type(my_array))
print(my_array[2,3])
print(my_array.dtype)
print(my_array.shape)
print(my_array.reshape(5,3))
my_array [1,3] = 900
print(my_array)
print(my_array[1:3,2:4])
print(my_array < 20 )
print(my_array[my_array < 20 ])
arr2 = nd.arange(1,101)
print(arr2)
arr_one = nd.ones((3,5))
print(arr_one)
arr_zero = nd.zeros((3,5))
print(arr_zero)
