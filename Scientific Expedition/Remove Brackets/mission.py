closed = ')]}'
opened = '([{'


def check(line: str) -> str:
    # while len(line) > 0 and line[-1] not in closed:
    #     print(line)
    #     print(line[-1])
    #     line = line[:-1]
    if len(line) <= 1:
        return ''
    # elif line[-1] in opened:
    #     return check(line[:-1])
    elif len(line) < 3:
        return line
    # print(line)
    while len(line) > 0 and line[-1] not in closed:
        # print(line)
        # print(line[-1])
        line = line[:-1]
    if len(line) == 0:
        return ''
    print(line)
    start = line.index(opened[closed.index(line[-1])])
    return check(line[:start]) + line[start] + check(line[start + 1: -1]) + line[-1]


def remove_brackets(line: str) -> str:
    newline = ''
    leave = [False] * len(line)
    for i in range(len(line) - 1, -1, -1):
        if leave[i]:
            continue
        if line[i] not in closed:
            continue
        for ii in range(i - 1, -1, -1):
            if line[ii] == opened[closed.index(line[i])] and not leave[ii]:
                leave[i] = True
                leave[ii] = True
                break
    for i in range(len(line)):
        if leave[i]:
            newline += line[i]
    return check(newline)
    # return newline


# def check(line: str) -> str:
#     closed = ')]}'
#     opened = '([{'
#     if len(line) == 1:
#         return ''
#     elif len(line) < 3:
#         return line
#     start = line.index(opened[closed.index(line[-1])])
#     return line[start] + check(line[start + 1: -1]) + line[-1]


if __name__ == "__main__":
    print("Example:")
    print(remove_brackets("(()()"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets("(()()") == "()()"
    assert remove_brackets("[][[[") == "[]"
    assert remove_brackets("[[(}]]") == "[[]]"
    assert remove_brackets("[[{}()]]") == "[[{}()]]"
    assert remove_brackets("[[[[[[") == ""
    assert remove_brackets("[[[[}") == ""
    assert remove_brackets("") == ""
    assert remove_brackets("[(])") == "()"
    print("Coding complete? Click 'Check' to earn cool rewards!")
