def to_encrypt(text, delta):
    # replace this for solution
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    newtext = ''
    for letter in text:
        if letter in alphabet:
            if alphabet.index(letter) + delta > len(alphabet):
                newtext += alphabet[(alphabet.index(letter) + delta) - len(alphabet)]
            elif alphabet.index(letter) + delta < 0:
                newtext += alphabet[(alphabet.index(letter) + delta) + len(alphabet)]
            else:
                newtext += alphabet[(alphabet.index(letter) + delta)]
        else:
            newtext += ' '

    return newtext


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
