def quick_sort(a: list):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        le_pivot = [i for i in a[1:] if i <= pivot]
        gt_pivot = [i for i in a[1:] if i > pivot]
        return quick_sort(le_pivot) + [pivot] + quick_sort(gt_pivot)

a = [20, 15, 59, 1, -8, 74, 33, 32]

print(quick_sort(a))