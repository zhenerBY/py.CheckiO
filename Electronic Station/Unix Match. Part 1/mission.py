def unix_match(filename: str, pattern: str) -> bool:
    import re
    # your code here
    # if '?' in pattern and '*' in pattern:
    #     return True
    seplist = []
    repattern = ''
    for letter in pattern:
        if letter == '*':
            repattern += '.*'
        elif letter == '?':
            repattern += '.'
        elif letter == '.':
            repattern += '\.'
        else:
            repattern += letter
    # print(repattern)
    if re.match(repattern, filename) is not None:
        return re.match(repattern, filename).group() == filename
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '*.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    assert unix_match('log12.txt', 'log??.txt') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
