from itertools import permutations
from typing import List, Tuple

def check_intersection(cir1:tuple, cir2:tuple) -> bool:
    distance = ((cir1[0] - cir2[0]) ** 2 + (cir1[1] - cir2[1]) ** 2) ** 0.5
    if distance <= cir1[2] + cir2[2] and max(cir1[2], cir2[2]) <= distance + min(cir1[2], cir2[2]):
        return True
    return False


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    count = 0
    tmpcount = 0
    for circle in circles[0]:
        circles_new = circle[1:]
        for i in circles_new:
            if check_intersection(circle, i):
                tmpcount += 1

    return 0


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
