def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Di chuyển các phần tử của phần đã sắp xếp lớn hơn key về phải
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Chèn key vào đúng vị trí
        arr[j + 1] = key

# Ví dụ sử dụng
example_array = [12, 11, 13, 5, 6]
insertion_sort(example_array)

print("Dãy số sau khi sắp xếp chèn:", example_array)