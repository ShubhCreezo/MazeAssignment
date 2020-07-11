import numpy

'''Here we take input of two integers separated by space then splits it to get dimensions of array.'''
# numpy.eye can make a identity matrix which we are converting to string and then applying replace to get output in particular format
print(str(numpy.eye(*map(int,input().split()))).replace('0',' 0').replace('1',' 1'))

'''This program is used to read input data and then we can perform operations on them'''
# If we are working with Python 2 then use raw_input()
# Sample input: 
# The first line contains two space separated integers, n and m.
# The next n lines contains m space separated integers of array a.
# The following n lines contains m space separated integers of array b.
# 1 4
# 4 5 6 7
# 7 8 4 6
# List comprehension is used
import numpy as np
n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')

'''Below code helps to find the runner up from a list of scores'''
# Given n scores 
n = int(raw_input())
arr = map(int, raw_input().split())

# enumerate can work with list indexes
if 2<=n<=10:
    arr.sort(reverse=True)
    for i,j in enumerate(arr):
        if arr[i+1]!=j:
            print(arr[i+1])
            break
''''''
            
            
       
