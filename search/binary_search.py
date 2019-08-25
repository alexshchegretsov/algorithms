def binary_search(a: list, n):
    low, high = 0, len(a) - 1
    while low <= high:        #Пока эта часть не сократится до одного элемента
        mid = (low + high) // 2
        guess = a[mid]
        if guess == n:
            return mid
        elif guess > n:
            high = mid - 1
        else:
            low = mid + 1
    return None

a = [8, 5, 4, 2, 1, 99]

print(binary_search(a, 99))
