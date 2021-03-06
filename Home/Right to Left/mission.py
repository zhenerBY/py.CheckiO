def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    ph = ""
    for ii, i in enumerate(phrases):
        # if not "left" in i:
        #     ph += str(i) + ',' if i != phrases[-1] else str(i)
        # else:
        ph += str(i).replace('right', 'left') + ',' if ii != len(phrases) - 1 else str(i).replace('right',
                                                                                                  'left')

    return ph


if __name__ == "__main__":
    print("Example:")
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
            left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    ), "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
