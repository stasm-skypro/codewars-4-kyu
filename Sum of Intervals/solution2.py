"""Intervals are represented by a pair of integers in the form of an array. The
first value of the interval will always be less than the second value. Interval
example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap,
we can treat the interval as [1, 5], which has a length of 4.
Your algorithm should be able to handle large intervals. All tested intervals
are subsets of the range [-1000000000, 1000000000]."""


def sum_of_intervals(intervals):
    n = len(intervals)
    i = 1
    while i < n:
        a = intervals[0]
        if intervals[1:]:
            b = intervals[i]
            if b[0] < a[-1]:
                c = tuple(sorted(a + b))
                intervals.remove(a)
                intervals.remove(b)
                intervals.insert(0, c)
                i = 0
                n = len(intervals)
        else:
            intervals.append(a)

        i = i + 1

    c = 0
    for interval in intervals:
        c = c + (interval[-1] - interval[0])

    return c


# testing case

print(sum_of_intervals([]) == 0)
print(sum_of_intervals([(1, 5)]) == 4)
print(sum_of_intervals([(1, 5), (6, 10)]) == 8)
print(sum_of_intervals([(1, 5), (1, 5)]) == 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5), (4, 8)]) == 9)
print(sum_of_intervals([(3, 5), (7, 10), (1, 4), (4, 8)]) == 9)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5), (4, 10), (5, 7)]) == 9)
print(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000)
print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030)
print(
    sum_of_intervals(
        [
            (194, 218),
            (-303, -205),
            (-368, -16),
            (-53, 44),
            (-164, 249),
            (-50, 484),
            (316, 481),
            (-467, 485),
        ]
    )
    == 952
)
# print(
#     sum_of_intervals(
#         [
#             (
#                 -461,
#                 -425,
#                 -412,
#                 -393,
#                 -360,
#                 -323,
#                 -230,
#                 -174,
#                 -124,
#                 -122,
#                 -27,
#                 7,
#                 23,
#                 44,
#                 60,
#                 74,
#                 76,
#                 98,
#                 99,
#                 159,
#                 167,
#                 204,
#                 219,
#                 221,
#                 256,
#                 429,
#                 443,
#                 472,
#                 481,
#                 498,
#             )
#         ]
#     )
#     == 914
# )
# print(
#     sum_of_intervals(
#         [
#             (
#                 -487,
#                 -474,
#                 -471,
#                 -450,
#                 -369,
#                 -277,
#                 -231,
#                 -127,
#                 -126,
#                 -97,
#                 -1,
#                 27,
#                 82,
#                 102,
#                 102,
#                 132,
#                 167,
#                 169,
#                 178,
#                 275,
#                 293,
#                 425,
#                 429,
#                 431,
#                 452,
#                 464,
#                 464,
#                 467,
#             )
#         ]
#     )
#     == 960
# )
# print(
#     sum_of_intervals(
#         [
#             (
#                 -452,
#                 -382,
#                 -281,
#                 -244,
#                 -209,
#                 -196,
#                 -174,
#                 -114,
#                 -110,
#                 -97,
#                 -37,
#                 -18,
#                 9,
#                 52,
#                 64,
#                 108,
#                 159,
#                 178,
#                 218,
#                 223,
#                 286,
#                 291,
#                 321,
#                 321,
#                 362,
#                 380,
#                 381,
#                 391,
#                 392,
#                 396,
#                 410,
#                 421,
#                 428,
#                 449,
#                 464,
#                 498,
#             )
#         ]
#     )
#     == 950
# )
