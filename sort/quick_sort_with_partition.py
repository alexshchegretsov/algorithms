def quick_sort(a: list):
    __partition(a, 0, len(a) - 1)


def __partition(a: list, left: int, right: int):
    if right <= left:
        return a
    k = i = left
    j = right
    pivot = a[left]
    while i <= j:
        if a[i] < pivot:
            a[k], a[i] = a[i], a[k]
            i += 1
            k += 1
        elif a[i] > pivot:
            a[j], a[i] = a[i], a[j]
            j -= 1
        else:
            i += 1
    __partition(a, left, k - 1)
    __partition(a, j + 1, right)


a = [7, 4, -11, 56, -90, -700, 56, -999]
quick_sort(a)
print(a)
