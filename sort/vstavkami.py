# Sortirovka vstavkami
# straight insertion


def sort_vstavka(a):
    for i in range(len(a)):
        x = a[i]
        j = i
        while (j > 0) and (x < a[j - 1]):
            a[j] = a[j - 1]
            j = j - 1
        a[j] = x

    return a


arr = [9, 5, 7, 3, 4, 2, 1, 0, 8, 6]
print(sort_vstavka(arr))

