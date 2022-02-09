def unix_match(filename: str, pattern: str) -> bool:
    import re
    if '[' in pattern:
        seq = pattern[pattern.index('['):pattern.index(']') + 1]
        # print('seq', seq)
        seq2 = seq
        if seq == '[]':
            return False
        elif seq == '[!]':
            pattern = pattern.replace('[!]', '\[!\]')
        elif seq2[1] == '!':
            seq2 = seq2.replace('!', '^')
            # print(seq2)
            pattern = pattern.replace(seq, seq2)
        # print(pattern)

    pattern = pattern.replace('*', '.*')
    pattern = pattern.replace('.', '\.')
    pattern = pattern.replace('?', '.')
    # your code here
    # print(pattern)
    return bool(re.fullmatch(pattern, filename))


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
