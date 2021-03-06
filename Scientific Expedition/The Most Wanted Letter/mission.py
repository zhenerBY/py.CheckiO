def checkio(text: str) -> str:
    # replace this for solution
    text = text.lower()
    count = 0
    let = 'z'
    for letter in text:
        if text.count(letter) > count and letter.isalpha():
            count = text.count(letter)
            let = letter
        elif text.count(letter) == count and letter.isalpha():
            if letter < let:
                let = letter
    return let


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
