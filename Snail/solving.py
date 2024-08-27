def snail(arr):
    # 1. Считываем первую строку.
    # 2. Поворачиваем матрицу на 90 гр. против часовой стрелки.
    # 3. Рекурсивно продолжаем пока не дойдём до 1 элемента в середине.

    result = []
    while arr:
        row = arr[0]
        result.extend(row)
        arr = arr[1:]
        arr = [list(row) for row in list(zip(*arr))[::-1]]

    return result


# test cases
array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(snail(array) == expected)

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(snail(array) == expected)
