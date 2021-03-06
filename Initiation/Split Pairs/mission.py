def split_pairs(a):
    # your code here
    a_list = []
    for i in range(0, len(a), 2):
        if len(a) % 2 == 1 and i == len(a) - 1:
            a = a[-1] + '_'
            a_list.append(a)
        else:
            a_list.append(a[i:i + 2])

    return a_list


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
