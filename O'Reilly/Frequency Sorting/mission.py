from typing import List


def frequency_sorting(numbers: List[int]) -> List[int]:
    # replace this for solution
    frenq = {}
    for num in numbers:
        frenq[num] = frenq.setdefault(num, 0) + 1
    sorted_second = dict(sorted(frenq.items(), key=lambda item: item[0]))
    frenq = dict(sorted(sorted_second.items(), key=lambda item: item[1], reverse=True))
    newnum = []
    for item in frenq:
        newnum.extend([item for x in range(frenq[item])])
    return newnum


if __name__ == "__main__":
    print("Example:")
    print(frequency_sorting([1, 2, 3, 4, 5]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert frequency_sorting([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Already sorted"
    assert frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]) == [
        4,
        4,
        4,
        3,
        3,
        11,
        11,
        7,
        13,
    ], "Not sorted"
    assert frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]) == [
        10,
        10,
        21,
        21,
        55,
        55,
        99,
        99,
    ], "Reversed"
    print("Coding complete? Click 'Check' to earn cool rewards!")
