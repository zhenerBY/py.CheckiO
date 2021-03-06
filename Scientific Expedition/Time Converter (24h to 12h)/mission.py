def time_converter(time):
    # replace this for solution
    h = int(time[:2])
    if h == 0:
        time = "12:00 a.m."
    elif h < 12:
        time = str(h) + ':' + time[-2:] + ' a.m.'
    elif h == 12:
        time = str(h) + ':' + time[-2:] + ' p.m.'
    elif h > 12:
        time = str(h - 12) + ':' + time[-2:] + ' p.m.'

    return time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
