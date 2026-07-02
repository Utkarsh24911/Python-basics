

# linear search 

def linear_search(arr,target):
    for i in range (len(arr)):
        if arr[i] == target:
            print("Element found at index:", i)

            return i 
        else:
            print("Element not found at index:",i)

arr=[11,2,4,8,5,6,7,3,9,10]
target = 10
linear_search(arr , target)



def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 25, 3, 47, 8, 91]

print(linear_search(arr, 47))  
print(linear_search(arr, 99))   
print(linear_search(arr, 10))  
print(linear_search(arr, 91))  



def search_name(names, target):

    target = target.lower()
    for i in range(len(names)):
        if names[i].lower() == target:
            return i
    return -1


names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

print(search_name(names, "charlie")) 
print(search_name(names, "ALICE"))   
print(search_name(names, "frank"))    
print(search_name(names, "Eve"))     



def find_all_occurrences(arr, target):

    result = []
    for i in range(len(arr)):
        if arr[i] == target:
            result.append(i)
    return result


arr = [5, 3, 7, 3, 9, 3, 1]

print(find_all_occurrences(arr, 3))  
print(find_all_occurrences(arr, 5))  
print(find_all_occurrences(arr, 10))


# binary search

def binary_search(arr , target):
    left = 0
    right = len (arr) - 1

    while left <= right :
        mid = (left + right)//2

        if arr[mid] == target:
            print("Element found at index:", mid)
            return mid
        
        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid -1

    return -1

sorted_arr = [2,3,4,5,6,7,8,9,10,11]
target = 5
result = binary_search(sorted_arr , target)


def binary_search(arr, target):
    low  = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1      
        else:
            high = mid - 1  

    return -1

arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]

print(binary_search(arr, 23))  
print(binary_search(arr, 2))   
print(binary_search(arr, 72))  
print(binary_search(arr, 10))   



def binary_search_recursive(arr, target, low, high):
   
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


arr = [1, 3, 7, 15, 22, 30, 44, 58]

print(binary_search_recursive(arr, 30, 0, len(arr)-1))  
print(binary_search_recursive(arr, 1,  0, len(arr)-1))  
print(binary_search_recursive(arr, 58, 0, len(arr)-1))  
print(binary_search_recursive(arr, 99, 0, len(arr)-1))   
