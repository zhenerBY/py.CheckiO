def backward_string_by_word(text: str) -> str:
    # your code here
    spaces = ''
    newtext = ''
    for sp in text:
        if sp == ' ':
            spaces += '&'
        else:
            spaces += " "
    for i in range(len(text.split())):
        if i < len(spaces.split()):
            newtext += text.split()[i][::-1] + spaces.split()[i]
        else:
            newtext += text.split()[i][::-1]

    return newtext.replace('&', ' ')


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
