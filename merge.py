def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = left[i]
            i = i + 1
            print(arr)
        else:
            arr[k] = right[j]
            j = j + 1
            print(arr)
        k = k + 1

    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1
        print(arr)
    while j < len(right):
        arr.append(right[j])
        j = j + 1
        k = k + 1
        print(arr)

arr = [8, 6, 5, 3, 0, 9, 5, 3]
arr1 = [8, 6, 5, 3, 0]
arr2 = [9, 5, 3]

merge(arr, arr1, arr2)
print(arr)
