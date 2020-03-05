import numpy
# This statement takes input of two integers separated by space then splits it to get dimensions of array.
# numpy.eye can make a identity matrix which we are converting to string and then applying replace to get output in particular format
print(str(numpy.eye(*map(int,input().split()))).replace('0',' 0').replace('1',' 1'))

# Below lines are used to read input data and then we can perform operations on them
# If we are working with Python 2 then use raw_input()
# Sample input: 
# The first line contains two space separated integers, n and m.
# The next n lines contains m space separated integers of array a.
# The following n lines contains m space separated integers of array b.
# 1 4
# 4 5 6 7
# 7 8 4 6
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')
