def bubble_sort(a: list) -> list:
    length = len(a)
    for i in range(length-1):   # -1 is for exclude repetitions, 3 cycles for 4 items
        swapped = False
        for j in range(length-1-i):
            if a[j] > a[j+1]:
                swapped = True
                a[j], a[j+1] = a[j+1], a[j]
        if not swapped:
            break
    return a

