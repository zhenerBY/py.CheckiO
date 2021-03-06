def frequency_sort(items):
    # your code here
    i_d = {}
    nitems = []
    for i in items:
        i_d.setdefault(i, 0)
        i_d[i] += 1
    keys_reverse = sorted(i_d, key=i_d.get, reverse=True)
    for n, i in enumerate(keys_reverse):
        for ii in range(i_d[i]):
            nitems.append(i)
    return nitems


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
