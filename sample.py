import numpy

# This statement takes input of two integers separated by space then splits it to get dimensions of array.
# numpy.eye can make a identity matrix which we are converting to string and then applying replace to get output in particular format
print(str(numpy.eye(*map(int,input().split()))).replace('0',' 0').replace('1',' 1'))
