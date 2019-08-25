from typing import Optional


def linear_search(seq: list, target: int) -> Optional[list]:
    for index, num in enumerate(seq):
        if num == target:
            return index
    return None

a = [3, 6 ,8 ,6 ,77, 99, 90]

print(linear_search(a, 99))
