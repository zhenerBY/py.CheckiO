# feel free to change table structure in any way

TABLE = '''
A 85-89%
A- 80-84%
B+ 77-79%
B 73-76%
B- 70-72%
C+ 67-69%
C 63-66%
C- 60-62%
D+ 57-59%
D 53-56%
D- 50-52%
'''


def ryerson_letter_grade(pct: int) -> str:
    table = {}
    if pct < 50:
        return 'F'
    if pct > 89:
        return 'A+'

    for i in TABLE.split('\n')[1:-1]:
        a, b = i.split()
        values = sorted(b[:-1].split('-'), reverse=True)
        val2 = [int(values[0])]
        for ii in range(int(values[0])-int(values[1])):
            val2.append(int(val2[ii])-1)
        table[a] = val2
    for i in table:
        if pct in table[i]:
            return i


if __name__ == '__main__':
    print("Example:")
    print(ryerson_letter_grade(45))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert ryerson_letter_grade(45) == "F"
    assert ryerson_letter_grade(62) == "C-"
    print("Coding complete? Click 'Check' to earn cool rewards!")
