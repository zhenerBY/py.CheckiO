def checkio(buildings):
    buildings_count = len(buildings)
    current_building = 0
    for house in buildings:
        area = (house[2] - house[0]) * house[4]
        area_remaining = area
        for i in range(buildings_count):
            if i == house:
                continue
            elif buildings[i][0] <= house[3]:
                continue
            elif buildings[i][2] > house[0] or buildings[i][0] < house[3]:
                continue





    # projection = []
    # for house in buildings:
    #     start = house[0]
    #     end = house[2]
    #     height = house[4]
    #     order = min(house[1], house[3])
    #     projection.append([start, end, height, order])
    # projection.sort(key=lambda x: x[3])
    # return projection


if __name__ == '__main__':
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"
