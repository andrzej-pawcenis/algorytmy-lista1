def counting_table(array, max_value):
    c_table = [0 * i for i in range(0, max_value +1)]
    for i in range(0, len(array)):
        c_table[arr[i]] += 1

    return c_table


arr = [5,6,0,8,3]
print(counting_table(arr, 8))
