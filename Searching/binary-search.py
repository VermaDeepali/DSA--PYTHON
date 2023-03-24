def binarySearch(arr, val):
    left = 0
    right = len(arr) - 1

    while(left <= right):
        midIndex = (left+right)//2
        midVal = arr[midIndex]
        
        if(midVal == val):
            return midIndex
        elif(midVal>val):
            right = midIndex-1
        else:
            left = midIndex + 1
    return -1
print(binarySearch(arr, val), "index")
