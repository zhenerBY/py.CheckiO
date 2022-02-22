def checkio(data: str) -> bool:
    if len(data) >= 10:
        result = False
        result2 = False
        result3 = False
        for letter in data:
            if letter.isdigit():
                result = True
            elif letter.isupper():
                result2 = True
            elif letter.islower():
                result3 = True
            if result and result2 and result3:
                return True
    return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
