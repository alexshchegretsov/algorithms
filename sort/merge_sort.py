# O(n*logn)
def merge(a: list, left: list, right: list) -> list:
    i = j = k = 0
    left_length = len(left)
    right_length = len(right)
    # implementing "finger sorting"
    while i < left_length and j < right_length:
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    # check if left-list have not visited elements during
    # previous cycle, if yes - append it's to a-list in-place
    while i < left_length:
        a[k] = left[i]
        i += 1
        k += 1
    # check if right-list have not visited elements during
    # previous cycle, if yes - append it's to a-list in-place
    while j < right_length:
        a[k] = right[j]
        j += 1
        k += 1

    return a


def merge_sort(a: list) -> list:
    if len(a) > 1:
        mid = len(a) // 2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])
        return merge(a, left, right)
    return a


a = [4, -1, 3, -9, 0, 64, 10, 9]
print(merge_sort(a))
