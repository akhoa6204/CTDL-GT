# def merge(n): 
#     if len(n) > 1: 
#         mid = len(n) // 2
#         left = n[: mid]
#         right = n[mid:]
#         merge(left)
#         merge(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 n[k] = left[i]
#                 i += 1
#             else : 
#                 n[k] = right[j]
#                 j += 1
#             k += 1
#         # so sánh với độ dài tránh trường hợp bên left = 2; right = 3
#         while i < len(left):
#             n[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             n[k] = right[j]
#             j += 1
#             k += 1
#     else :
#         return n

def merge(arr): 
    if len(arr) < 2: return arr 
    else: 
        left = arr[: (len(arr) // 2)] 
        right = arr[(len(arr) // 2) :]
        merge(left)
        merge(right) 
        i = j = k = 0 
        while i < len(left) and j < len(right):
            if left[i] < right[j]: 
                arr[k] = left[i] 
                i += 1
            else: 
                arr[k] = right[j]
                j += 1 
            k += 1 
        while i  < len(left): 
            n[k] = left[i]
            i += 1 
            k += 1 
        while j < len(right): 
            n[k] = right[j]
            j += 1 
            k += 1  

n = [64, 34, 25, 12, 22, 11, 90]
merge(n)
print(n)
        