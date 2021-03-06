def sum_consecutives(a):
    answer = []
    tmpresult = 0
    for i in range(len(a)):
        if i == 0:
            num = a[i]
            tmpresult = a[i]
        else:
            if a[i] == num:
                tmpresult += num
            else:
                num = a[i]
                answer.append(tmpresult)
                tmpresult = a[i]
    if tmpresult != 0:
        answer.append(tmpresult)
    return answer


if __name__ == '__main__':
    print("Example:")
    print(list(sum_consecutives([1, 1, 1, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(sum_consecutives([1, 1, 1, 1])) == [4]
    assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
    assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
    assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
    assert list(sum_consecutives([1])) == [1]
    assert list(sum_consecutives([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
