def s_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        buff = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = buff
        print(arr)

arr = [5,6,0,8,8,3]
s_sort(arr)
