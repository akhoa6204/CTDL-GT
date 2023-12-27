def interchange(arr): 
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]: 
                arr[i], arr[j] = arr[j], arr[i]

def merge(arr):
    if len(arr) < 2: return arr
    else: 
        left = arr[: (len(arr) // 2)]
        right = arr[(len(arr) // 2) :]
        merge(left)
        merge(right)
        i= j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                arr[k] = left[i]
                i += 1
            else: 
                arr[k] = right[j]
                j += 1 
            k += 1 
        while i < len(left): 
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1 

def quick(arr): 
    if len(arr) < 2: return arr 
    else: 
        mid = [x for x in arr if x == arr[len(arr) // 2]]
        left = [x for x in arr if x < arr[len(arr) // 2]]
        right = [x for x in arr if x > arr[len(arr) // 2]]
        return quick(left) + mid + quick(right) 

def buble(arr): 
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection(arr): 
    for i in range(len(arr)): 
        min = i
        for j in range(i, len(arr)): 
            if arr[j] < arr[min]: 
                min = j 
        arr[i], arr[min] = arr[min], arr[i]

def insertion(arr): 
    for i in range(1, len(arr)): 
        cur = arr[i]
        j = i - 1
        while j >= 0 and cur < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur

arr = [12, 1 ,2 ,3, 4, 112, 13 ,12123,1231243,12,1231,45,45431231,2343245,1431314]
print(quick(arr))
arr = [12, 1 ,2 ,3, 4, 112, 13 ,12123,1231243,12,1231,45,45431231,2343245,1431314]
selection(arr)
print(arr)
arr = [12, 1 ,2 ,3, 4, 112, 13 ,12123,1231243,12,1231,45,45431231,2343245,1431314]
interchange(arr)
print(arr)
arr = [12, 1 ,2 ,3, 4, 112, 13 ,12123,1231243,12,1231,45,45431231,2343245,1431314]
merge(arr)
print(arr)
arr = [12, 1 ,2 ,3, 4, 112, 13 ,12123,1231243,12,1231,45,45431231,2343245,1431314]
insertion(arr)
print(arr)
