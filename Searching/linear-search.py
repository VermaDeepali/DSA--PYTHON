# linear search
arr = [10,12,24,29,39,40,51,56,69]

def linearSearch(arr, n, val):
    pos = -1
    for i in range(0, n):
        if(arr[i]==val):
            pos = i
            return pos
    return "element not present in the array."

print(linearSearch(arr, 8, 24))  # output: 2
