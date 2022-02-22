def long_repeat(line: str) -> int:
    if len(line) <= 1:
        return len(line)
    count = 1
    counttmp = 1
    current_letter = line[0]
    for i in range(1, len(line)):
        if line[i] == current_letter:
            counttmp += 1
            continue
        else:
            if counttmp > count:
                count = counttmp
            counttmp = 1
            current_letter = line[i]
    if counttmp > count:
        count = counttmp
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
