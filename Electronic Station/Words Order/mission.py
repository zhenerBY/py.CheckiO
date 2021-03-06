def words_order(text: str, words: list) -> bool:
    # your code here
    textlist = text.split()
    newlist = []
    newlistcontrol = []
    counter = 0
    for i in words:
        if i in textlist:
            if textlist.index(i) + counter in newlistcontrol:
                return False
            if i in newlist:
                return False
            newlistcontrol.append(textlist.index(i) + counter)
            newlist.append(textlist.pop(textlist.index(i)))
            counter += 1
        else:
            return False
    if newlistcontrol == sorted(newlistcontrol):
        return True

    return False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
                       ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
                       ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
                       ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
                       ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

# ("hi world world im here",["world","world"])
# Right result:false
