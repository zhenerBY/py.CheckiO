from typing import Tuple


def follow(instructions: str) -> Tuple[int, int]:
    coor = [0, 0]
    for i in instructions:
        if i == 'f':
            coor[1] += 1
        elif i == 'b':
            coor[1] -= 1
        elif i == 'r':
            coor[0] += 1
        elif i == 'l':
            coor[0] -= 1

    return (coor[0], coor[1])


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
