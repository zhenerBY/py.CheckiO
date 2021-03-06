def safe_pawns(pawns: set) -> int:
    num_safe = 0
    l = ("a", "b", "c", "d", "e", "f", "g", "h")
    pawns_n = []
    for i in pawns:
        pawns_n.append((l.index(i[0]) + 1, int(i[1])))
    for pawn in pawns_n:
        for i in pawns_n:
            if pawn[1] - i[1] == 1:
                if abs(pawn[0] - i[0]) == 1:
                    num_safe += 1
                    break
    return num_safe


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
