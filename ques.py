# Q)  print maximum and minimum no. 

numbers=[42,17,89,8,55,91,23]

max_value = numbers[0]
min_value = numbers[0]

for num in numbers:
    if num>max_value:
        max_value = num

    if num<min_value:
        min_value = num 

    
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")


# Q) reversal of array without creating new array 
# 
arr=[1,7,34,5,6,354]

left=0
right=len(arr)-1

while left<right:
    arr[left],arr[right]=arr[right],arr[left]
    left+=1
    right-=1

print(arr)

# check wheter array is sorted


arr=[1,2,7,4,5]
sorted = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted= False
        
        break
print(sorted)


# putting all zeros of an array at the end

def move_zeros_to_end(arr):

    pos = 0

    for i in range (len(arr)):
        if arr[i] != 0:
            arr[pos] , arr[i] = arr[i] , arr[pos]
            pos += 1

my_list = [1,0,4,0,5,0,]
move_zeros_to_end(my_list)
print(my_list)

# print second largest element

def second_largest(arr):
    largest= -1
    secondlargest = -1
    
    for i in range(len(arr)):
        if arr[i]> largest:
            largest = arr[i]
            
        
    for i in range(len(arr)):
        if arr[i] >secondlargest and arr[i] !=largest:
            
            secondlargest=arr[i]
            
    return f" second largest element: {secondlargest}"

arr=[10,11,12,13]
print(second_largest(arr))



# 3. Reverse an array

def reverse(arr):
    
    left =0
    right = len(arr)-1
    
    while left < right:
        arr[left],arr[right]=arr[right],arr[left]
        
        left+=1
        right-=1
    return arr

arr=[1,2,3,4,5]
print(reverse(arr))
    

# 4 Reverse array in groups.

def reverseInGroups(arr, k):
    i = 0
    n = len(arr)  
    
    while i < n:
        left = i 

        
        right = min(i + k - 1, n - 1) 
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        i += k
    return arr


arr = [1, 2, 3, 4, 5, 6, 7, 8] 
k = 3
print(reverseInGroups(arr, k))


# 5.Rotate an array

def rotation(arr,d):
    
    for i in range(0,d):
        
        element= arr.pop(0)
        arr.append(element)
        
    return arr

arr=[1,2,3,4,5]

print(rotation(arr,2))

# 6.Three Great Candidate

def maximum_triplet(arr):
    if len(arr)  < 3:
        return "Array must have atleast 3 elements"
    
    arr.sort()

    candidate_1 = arr[-1]*arr[-2] *arr[-3]
    candidate_2 = arr[0]*arr[1] *arr[-1]
   
    
    return max (candidate_1 , candidate_2)


print(maximum_triplet([1,2,3,4,5]))

print(maximum_triplet([-10,-10,1,2,3]))


# Search in a String List


def search_string_list(names,target):
    target_lower = target.lower()

    index = 0

    for name in names:
        if name.lower() == target_lower:
            return index
        index += 1
    return -1 

name_list = ["Alice","Bob","Charlie","Diana","Eve"]

print(search_string_list(name_list , "charlie"))
print(search_string_list(name_list , "frank"))
print(search_string_list(name_list , "BOB"))


# finding all occurance

def find_all_occurance(arr , target):
    result_list = []

    for i in range(len(arr)):
        if arr[i] == target:
            result_list.append(i)

    return result_list

arr = [5,3,7,3,9,3,1]

print(find_all_occurance(arr , 3))


# Search in a list of dictionaries

def find_student_grade(students , target):
    for student in students:
        if student["name"] == target:
            return student["grade"]
        
    return "Not Found"

students_list = [
      {"name": "Alice", "grade": "A"},
      {"name": "Bob",   "grade": "B+"},
      {"name": "Carol", "grade": "A-"},
      {"name": "Dave",  "grade": "C"},
  ]

print(find_student_grade(students_list ,"Carol"))


# Count target occurance

def count_occurance(arr,target):
    count = 0
    
    for element in arr:
        if element == target:
            count+=1

    return count 

arr =[4, 2, 4, 4, 1, 7, 4, 9]

print(count_occurance(arr , 4))

print(count_occurance(arr,6))



