from typing import Union
import time


def sun_angle(time: str) -> Union[int, str]:
    # replace this for solution
    time = int(time[:2]) + float('.' + time[3:]) / 60 * 100
    if time < 6 or time > 18:
        return "I don't see the sun!"
    return round((time - 6) * 180 / 12, 2)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
