def bubbleSort(arr):
    n = len(arr)
    for _ in range(n - 1):
        for i in range(n - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
    
print(bubbleSort([11, 4, 3, 7, 6, 1])) # output: [1, 3, 4, 6, 7, 11]
