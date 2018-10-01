def buble_sort(arr):
    len_array = len(arr)
    for i in range(len_array):
        for j in range(0, (len_array-i-1)):
            if arr[j] > arr[j+1]:
                k = arr[j+1]
                arr[j+1] = arr[j]
                arr[j]=k
    res_arr = arr
    return res_arr


arr = [9, 4, 6, 5, 8, 7, 3, 2, 1, 0]
print(buble_sort(arr))




