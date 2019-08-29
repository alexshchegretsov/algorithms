def insertion_sort(a: list) -> list:
    for i in range(1, len(a)):
        while i > 0 and a[i-1] > a[i]:
            a[i], a[i-1] = a[i-1], a[i]
            i -= 1
    return a

a = [7,4,-11, 56, -90, -700, 56]
print(insertion_sort(a))