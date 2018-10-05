# sort vyborom
# search min by linear and change with current


def main_sort(my_arr):
    for ind in range(len(my_arr)):
        minimum = min(my_arr[ind:])
        ind_min = my_arr.index(minimum)
        my_arr[ind_min] = my_arr[ind]
        my_arr[ind] = minimum
        # pass
        # return my_arr
    return my_arr


our_arr = [8, 4, 3, 7, 5, 2, 1, 9, 6, 0]
print(main_sort(our_arr))
