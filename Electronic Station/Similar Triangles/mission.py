from typing import List, Tuple

Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    f = []
    s = []
    f.append(((coords_1[0][0] - coords_1[1][0]) ** 2 + (coords_1[0][1] - coords_1[1][1]) ** 2) ** 0.5)
    f.append(((coords_1[1][0] - coords_1[2][0]) ** 2 + (coords_1[1][1] - coords_1[2][1]) ** 2) ** 0.5)
    f.append(((coords_1[2][0] - coords_1[0][0]) ** 2 + (coords_1[2][1] - coords_1[0][1]) ** 2) ** 0.5)
    s.append(((coords_2[0][0] - coords_2[1][0]) ** 2 + (coords_2[0][1] - coords_2[1][1]) ** 2) ** 0.5)
    s.append(((coords_2[1][0] - coords_2[2][0]) ** 2 + (coords_2[1][1] - coords_2[2][1]) ** 2) ** 0.5)
    s.append(((coords_2[2][0] - coords_2[0][0]) ** 2 + (coords_2[2][1] - coords_2[0][1]) ** 2) ** 0.5)
    f.sort()
    s.sort()
    return round(f[0] / s[0], 10) == round(f[1] / s[1], 10) == round(f[2] / s[2], 10)


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
