def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    # your code here
    alb = 'abcdefghijklmnopqrstuvwxyz'
    alb_new = set()
    for letter in text.lower():
        if letter in alb:
            alb_new.add(letter)
    return set(alb) == alb_new


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
