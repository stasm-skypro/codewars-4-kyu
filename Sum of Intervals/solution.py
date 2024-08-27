def sum_of_intervals(intervals):
    s = []
    for interval in intervals:
        s.extend(list(range(interval[0], interval[1])))

    mask = list(range(min(s), max(s) + 1))

    c = sum((1 for x in mask if x in s))
    # print(c)
    return c


# testing case
print(sum_of_intervals([(1, 5)]) == 4)
print(sum_of_intervals([(1, 5), (6, 10)]) == 8)
print(sum_of_intervals([(1, 5), (1, 5)]) == 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5), (4, 8)]) == 9)
