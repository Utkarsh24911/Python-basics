# bubble sort 

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]

    return arr

arr = [11,2,4,8,5,6,7,3,9,10,1]

sorted_arr = bubble_sort(arr)
print(sorted_arr)



# insertion_sort


def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i]
        j=i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr = [11,2,4,8,5,6,7,3,9,10]
sorted_arr = insertion_sort(arr)
print(sorted_arr)    


# selection sort 

arr = [2,10,8,1,4,6,3,5,7,9]

def selection_sort(arr):
    n=len(arr)

    for i in range(n):
        min_index = i

        for j in range (i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]

    return arr

print("Unsorted array:", arr)
sorted_arr = selection_sort(arr)
print("Sorted array:",sorted_arr)





                
            

