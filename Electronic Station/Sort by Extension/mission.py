from typing import List
from operator import itemgetter


def sort_by_ext(files: List[str]) -> List[str]:
    f = sorted(files, key=lambda x: x[:x.rfind('.')])
    return sorted(f, key=lambda x: x[x.rfind('.'):] if x.index('.') != 0 or x.count('.') > 1 else '')


if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    print("Coding complete? Click 'Check' to earn cool rewards!")

# ([".config","my.doc","1.exe","345.bin","green.bat","format.c","no.name.","best.test.exe"])
# Right result:[".config","no.name.","green.bat","345.bin","format.c","my.doc","1.exe","best.test.exe"]


# (["1.cad","2.bat","1.aa","1.bat"])
# Right result:["1.aa","1.bat","2.bat","1.cad"]
