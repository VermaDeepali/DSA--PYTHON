def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        small = i
        for j in range(i+1, n):
            if arr[j] < arr[small]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    return arr

print(selectionSort([12, 31, 25, 8, 32, 17])) # output: [8, 12, 17, 25, 31, 32]
