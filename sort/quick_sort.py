def quick_sort(a: list) -> list:
    # base case
    if len(a) < 2:
        return a
    # recursive case
    else:
        pvt = a[0]
        # subarray where numbers less or equal then pvt
        le_pvt = [i for i in a[1:] if i <= pvt]
        # subarray where numbers strictly greater then pvt
        gt_pvt = [i for i in a[1:] if i > pvt]
        return quick_sort(le_pvt) + [pvt] + quick_sort(gt_pvt)


a = [2, 6, 0, -56]

print(quick_sort(a))