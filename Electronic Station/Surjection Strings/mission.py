def isometric_strings(a, b):
    # your code here
    new = ''
    for i in a:
        new += b[a.index(i)]
    return new == b


if __name__ == "__main__":
    print("Example:")
    print(isometric_strings("add", "egg"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings("add", "egg") == True
    assert isometric_strings("foo", "bar") == False
    assert isometric_strings("", "") == True
    assert isometric_strings("all", "all") == True
    assert isometric_strings("gogopy", "doodle") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
