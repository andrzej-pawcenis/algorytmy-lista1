def quick_sort(arr, _min, _max):
    if _min < _max:
        p_index = partition(arr, _min, _max)
        quick_sort(arr, _min, p_index - 1)
        print(f"lewy fragment: {arr}")
        quick_sort(arr, p_index + 1, _max)
        print(f"prawy fragment: {arr}")

def partition(arr, _min, _max):
    pivot = arr[_max]
    i = _min - 1
    for j in range(_min, _max - 1):
        if arr[j] < pivot:
            i = i + 1
            buff = arr[i]
            arr[i] = arr[j]
            arr[j] = buff
    buff = arr[i + 1]
    arr[i + 1] = arr[_max]
    arr[_max] = buff
    return i + 1

arr = [5,6,0,8,3]
print(f"dane wejsciowe: {arr}")
quick_sort(arr, 0, len(arr)-1)
print(f"wynik: {arr}")
