from random import randint as rd
import time


def quick_sort(a: list) -> list:
    if len(a) > 1:
        pvt = a[0]
        # print(f'pivot: {a[0]}, in {a}')
        # subarray where numbers less or equal then pvt
        le_pvt = [i for i in a[1:] if i <= pvt]
        # subarray where numbers strictly greater then pvt
        gt_pvt = [i for i in a[1:] if i > pvt]
        # print(f'less: {le_pvt}, greater: {gt_pvt}')
        return quick_sort(le_pvt) + [pvt] + quick_sort(gt_pvt)
    return a

