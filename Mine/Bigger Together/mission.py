from itertools import permutations
from typing import List


def bigger_together(ints: List[int]) -> int:
    # all = list(permutations(ints))
    # maxx = int(''.join(map(str, max(all, key=lambda x: int(''.join(map(str, x)))))))
    # minn = int(''.join(map(str, min(all, key=lambda x: int(''.join(map(str, x)))))))
    # maxx = minn = int(''.join(map(str, ints)))
    # for i in permutations(ints):
    #     ii = int(''.join(map(str, i)))
    #     if ii > maxx:
    #         maxx = ii
    #     if ii < minn:
    #         minn = ii
    # return maxx - minn
    swap = 1
    while swap:
        swap = 0
        for i in range(len(ints)-1):
            if int(str(ints[i])+str(ints[i+1])) < int(str(ints[i+1])+str(ints[i])):
                swap, ints[i], ints[i+1] = 1, ints[i+1], ints[i]
    strints = [str(ints[i]) for i in range(len(ints))]
    return int("".join(strints)) - int("".join(strints[::-1]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    assert bigger_together([1, 2, 3, 4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print('Done! I feel like you good enough to click Check')
