import numpy as np
print('numpy',np.__version__)

#Checking the available methods
#print(dir(np))

python_list = [1,2,3,4,5]

two_dimensional_list=[[0,1,2],[3,4,5],[6,7,8]]
print("two dimensional list",two_dimensional_list)

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list=np.array(python_list)
print(type (numpy_array_from_list))   
print(numpy_array_from_list)

numpy_array_from_list2=np.array(python_list,dtype=float)
print(numpy_array_from_list2)

numpy_bool_array=np.array([0,-1,1,0,-3,2,0], dtype=bool)
print(numpy_bool_array)

numpy_two_dimensional_list=np.array(two_dimensional_list)
print(numpy_two_dimensional_list)

#Converting numpy array to list
np_to_list=numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

# Numpy array from tuple
python_tuple=(1,2,3,4,5)
numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple)
"""
#Shape of numpy array
The shape method provide the shape of the array 
as a tuple. The first is the row and the second 
is the column. If the array is just one dimensional 
it returns the size of the array.
"""
nums = np.array([1, 2, 3, 4, 5])
print('shape of nums: ', nums.shape)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)

#Data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array.dtype)
print(float_array.dtype)

#Size of a numpy array

print('The size:', numpy_array_from_list.size) # 5
print('The size:', numpy_two_dimensional_list.size)

#Matematical Operation
"""
NumPy array is not like exactly like python list. 
To do mathematical operation in Python list 
we have to loop through the items 
but numpy can allow to do any mathematical operation 
without looping. Mathematical Operation:

Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modules (%)
Floor Division(//)
Exponential(**)
"""
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)

#Converting types
#int to float
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
#float to int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
#int to boolean
np.array([-3, -2, 0, 1,2,3], dtype='bool')
#int to str
numpy_float_list=np.array([1., 2., 3., 4.])
numpy_str_list=numpy_float_list.astype('int').astype('str')
print(numpy_str_list)

#Multi dimensional Arrays
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

#Getting item from a numpy array
print(two_dimension_array)
first_row=two_dimension_array[0]
second_row=two_dimension_array[1]
third_row=two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
first_column=two_dimension_array[:,0]
second_column=two_dimension_array[:,1]
third_column=two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)

#Slicing
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
#reverse rows
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(two_dimension_array)
two_dimension_array=two_dimension_array[::-1,::-1]
print(two_dimension_array)
#Cambiando elementos
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C'C
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)
# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
twoes = numpy_ones * 2
print(twoes)

#Reshape
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
""" Los valore de reshape multiplicados debend
dar el valor de size(cantidad de elementos)
del array original
"""
print(reshaped)

#Flattened
flattened = reshaped.flatten()
print(flattened)
print(type(flattened))

#Horizontal stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two)
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

#Random numbers
random_float = np.random.random()
print(random_float)
random_floats = np.random.random(5)
print(random_floats)
# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
print(random_int)
# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
print(random_int)
# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

#Generation random number con parametros de estadistica
# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(50, 5, 10)
print(normal_array)

#Numpy and Statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#plt.hist(normal_array, color="grey", bins=50)
#plt.show()

#MATRIX IN NUMPY
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)
np.asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

#NUMPY numpy.arange()
lst = range(0, 11, 2)
for l in lst:
    print(l)
# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
print(whole_numbers)
odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)
even_numbers = np.arange(2, 20, 2)
print(even_numbers)
#Creating sequence of numbers using linspace
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
print(np.linspace(1.0, 5.0, num=10))
# not to include the last value in the interval
np.linspace(1.0, 5.0, num=5, endpoint=False)

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

print(np.logspace(2, 4.0, num=5))

#Creat matriz with complex number
x = np.array([1,2,3], dtype=np.complex128)
print(x)
print(x.itemsize)

#NUMPY STATISTICA FUNCTIONS WITH EXAMPLE

## min, max, mean, median, sd
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())

print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))


#Create repating sequences
a=[1,2,3]
# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('min: ', np_normal_dis.min())
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="grey", bins=21)
#plt.show()

#Algebra linear
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
print(np.dot(f, g)) # 23

#Multiplicación de matrices
### Matmul: matruc product of two arrays
h = np.array([[1,2],[3,4]])
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
print(np.matmul(h, i))

print(np.linalg.det(i))

Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

print(Z)

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)

np_arr = np.array(range(0, 11))
print(np_arr + 2)
"""
We use linear equation for quantities which have 
linear relationship. Let's see the example below:
"""
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
#plt.show()

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.displot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()







