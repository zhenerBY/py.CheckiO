def checkio(radius):
    all = ((3 // 1 + 1 if 3 % 1 != 0 else 3 // 1) * 2) ** 2
    return [0, 0]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
