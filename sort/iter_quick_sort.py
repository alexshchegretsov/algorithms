def partition(a, start, end):
    follower = leader = start
    while leader < end:
        if a[leader] <= a[end]:
            a[follower], a[leader] = a[leader], a[follower]
            follower += 1
        leader += 1
    a[follower], a[end] = a[end], a[follower]
    return follower


def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p - 1)
    _quicksort(xs, p + 1, end)


def quicksort_2(xs):
    _quicksort(xs, 0, len(xs) - 1)


