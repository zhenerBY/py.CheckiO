def translate(text: str) -> str:
    # your code here
    vowels = "aeiouy"
    i = 0
    newtext = ''
    while i < len(text):
        if text[i] in vowels:
            newtext += text[i]
            i += 3
        elif text[i] == ' ':
            newtext += text[i]
            i += 1
        else:
            newtext += text[i]
            i += 2
    return newtext


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
