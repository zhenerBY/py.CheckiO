def checkio(text, word):
    word = word.lower()
    text = text.replace(' ', '').lower().split('\n')
    maxlen = max(len(x) for x in text)
    for i, string in enumerate(text):
        if word in string:
            return [i + 1, string.index(word) + 1, i + 1, string.index(word) + len(word)]
    text = list(map(list, text))
    text_column = []
    for i in range(maxlen):
        string = ''
        for ii in range(len(text)):
            if i < len(text[ii]):
                string += text[ii][i]
            else:
                string += '~'
        text_column.append(string)
    for i, string in enumerate(text_column):
        if word in string:
            return [string.index(word) + 1, i + 1, string.index(word) + len(word), i + 1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
print("Coding complete? Click 'Check' to earn cool rewards!")
