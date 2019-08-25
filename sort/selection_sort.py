def seletion_sort(a: list) -> list:
    """
    During each iteration the smallest element's
    index is found and swapped with the corresponding
    position.
    First smaller swapped with first element.
    Second smaller swapped with second element.
    etc
    """
    length = len(a)
    for i in range(length-1):
        min_id = i
    # don't care about i-index element, cauz we're start from i+1 and
    # doesn't matter would be swapped with i-index element 
        for j in range(i+1, length):
            if a[j] < a[min_id]:
                min_id = j
        a[i], a[min_id] = a[min_id], a[i]
    return a
