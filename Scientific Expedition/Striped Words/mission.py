def checkio(line: str) -> str:
    import re
    vowels = 'AEIOUY'.lower()
    consonants = 'BCDFGHJKLMNPQRSTVWXZ'.lower()
    line = line.strip('.!?').lower()
    wordlist = re.split(' |\.|,', line)
    count = 0
    for word in wordlist:
        vow = None
        for num, letter in enumerate(word):
            if word.isalpha() is False:
                break
            if vow is None:
                if letter in vowels:
                    vow = True
                elif letter in consonants:
                    vow = False
            elif vow == True:
                if letter in consonants:
                    vow = False
                else:
                    break
            elif vow == False:
                if letter in vowels:
                    vow = True
                else:
                    break
            if len(word) == 1:
                break
            if len(word) - 1 == num and vow is not None:
                count += 1
    return count


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
