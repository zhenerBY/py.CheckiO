def from_camel_case(name: str) -> str:
    newname = ''
    for num, letter in enumerate(name):
        if num == 0:
            if letter == name[num].upper():
                newname += letter.lower()
            else:
                newname += name[num]
        elif letter == name[num].upper():
            newname += '_' + letter.lower()
        else:
            newname += letter
    return newname


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
