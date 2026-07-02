
arr = [10 , 20 , 30 , 40]

print(arr[1])
arr[1] = 99

arr.append(50)
arr.insert (2,55)

arr.pop()
arr.pop(1)
arr.remove(55)
del arr[0]

idx = arr.index (30)
found = 30 in arr 
cnt = arr.count(30)


array = []
print(array)

# #initial values
array_1 = [1 , 2 , 3, 4 , 5 ]
print(array_1)

array_2 = [ x*2 for x in range(1 , 6)]
print(array_2)


array_3 = list(range(1,11))
print(array_3)


array_4 = [0] * 5
print(array_4)


import array 

val = array.array('i',[1,2,3,4,5,6])

for i in range(0,6):
     print(val[i],end=" ")

    # OR

import array as arr

val = arr.array('i',[1,2,3,4,5,6])

for x in val:
     print(x,end=",")

    #   OR

# from array import *

val =array('i' ,[1,2,3,4,5,6,7,8,9,10])

for i in range(0,len(val)):
     print(val[i],end=" ")

print('\n')

for x in val:
     print(x,end=",")


print('\n')


print(val.typecode)

val.reverse()

for i in range (0,len(val)):
     print(val[i] , end=',')

val.insert(2,39)
val.append(101)
val[4]=44

for i in range (0,len(val)):
     print(val[i] , end=' ')


# Make a new array and insert the values of old arrays in it

from array import*

val=array('i' , [1,2,3,4,5,6,7,8,9])

copyArray=array(val.typecode,(x*2 for x in val))

for i in range (0,len(val)):
    print(copyArray[i] , end=" , ")


print('\n')

copyArray.reverse()
for i in range (0,len(val)):
    print(copyArray[i] , end=" , ")

copyArray.pop(3)
for i in range (0,len(copyArray)):
    print(copyArray[i] , end=" , ")

print('\n')

copyArray.remove(4)
for i in range (0,len(copyArray)):
    print(copyArray[i] , end=" , ")


# SLICING

from array import*

val = array('i' , [1,2,3,4,5,6,7,8,9])

abc = val[2 : 6]

for i in range (0,len(abc)):
    print(abc[i] , end=' ')

print()

abc = val[2 : -4]

for i in range (0,len(abc)):
    print(abc[i] , end=' ')

print()

abc = val[::]

for i in range (0,len(abc)):
    print(abc[i] , end=' ')


from array import*

arr = array('i' , [])

n = int(input("Enter a number:"))

for i in range(0,n):
    arr.append(int(input("Enter next input:")))


for x in arr:
    print(x,end=" ")

from array import*

arr = array('i' , [12,123,124,445,66,77])

i=arr.index(66)

print(i)


# questions 


# 1. Sum of all elements — Given an array of integers, return the sum without using sum().

from array import*

arr=array('i' , [11,22,33,44,55])

total_sum = 0

for x in arr:
    total_sum += x

print("Sum of all elements:" , total_sum)


# 2. Find the largest element — Find the max element in an array without using max().

from array import*

a = array('i' , [12,104,6,57,98,1])

max_element = a[0]

for element in a :
    if element > max_element:
        max_element = element

print("Largest element:" , max_element)


# 3. Reverse an array — Reverse an array without using .reverse() or slicing [::-1].


from array import*

arr = array('d' , [1.2 , 3.4 , 3.9 , 2.5 , 6.7 , 1.1])

left = 0
right = len(arr) -1

while left<right:
    arr[left], arr[right] = arr[right] , arr[left]

    left += 1
    right -= 1

print(arr)

