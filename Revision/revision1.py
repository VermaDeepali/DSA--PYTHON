# Searching

# Linear Search

def linearSearch(array, value):
    pos = -1
    n = len(array)
    for i in range(n):
        if(array[i]==value):
            pos = i 
            return pos
    if(pos == -1):
        return "Val not exist in array"
        
array = [99,44,33,67,34,23]
value = 23

print("Linear: ",linearSearch(array,value))

# Time Complexity

# Best Case - O(1)
# Avg Case - O(n)
# Worst Case - O(n)

# Space Complexity - O(1)



# Binary Search 

arr = [3,6,7,8,44,23]
lower = 0
upper = len(arr) - 1
val = 7

def binarySearch(arr, upper, lower, val):
    beg = lower
    end = upper
    pos = -1
    
    while(beg <=end):
        mid = (beg+end)//2
        if(arr[mid] == val):
            pos = mid
            return pos
        elif(arr[mid]>val):
            end = mid -1
        else:
            beg = mid+1 
    if(pos == -1):
        return "val not exist in array"
        
    return pos
    
print("Binary: ", binarySearch(arr, upper, lower, val))

# Time Complexity

# Best Case - O(1)
# Avg Case - O(logn)
# Worst Case - O(logn)

# Space Complexity - O(1)


# Sorting

# Bubble Sort 

def bubbleSort(array):
    n = len(array)
    for _ in range(n-1):
        for i in range(n-1):
            if(array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
    return array
array1 = [99,44,33,67,34,23]    
print("Bubble", bubbleSort(array1))


"""
Output: 

Linear:  5
Binary:  2
Bubble [23, 33, 34, 44, 67, 99]
"""
