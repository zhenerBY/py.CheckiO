def to_camel_case(name: str) -> str:
    # replace this for solution
    key = True
    newname = ''
    for num, letter in enumerate(name):
        if letter == '_':
            key = True
        elif key:
            newname += letter.upper()
            key = False
        else:
            newname += letter
    return newname


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
