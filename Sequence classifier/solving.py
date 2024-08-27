"""A series or sequence of numbers is usually the product of a function and can
either be infinite or finite.
In this kata we will only consider finite series and you are required to return
a code according to the type of sequence:
Code 	Type 	Example
0 	unordered 	[3,5,8,1,14,3]
1 	strictly increasing 	[3,5,8,9,14,23]
2 	not decreasing 	[3,5,8,8,14,14]
3 	strictly decreasing 	[14,9,8,5,3,1]
4 	not increasing 	[14,14,8,8,5,3]
5 	constant 	[8,8,8,8,8,8]
You can expect all the inputs to be non-empty and completely numerical
arrays/lists - no need to validate the data; do not go for sloppy code, as
rather large inputs might be tested.
Try to achieve a good solution that runs in linear time; also, do it
functionally, meaning you need to build a pure function or, in even poorer
words, do NOT modify the initial input!
"""


def sequence_classifier1(arr):
    """Решение на уровне junior разработчика."""
    if all([x == arr[0] for x in arr]):
        return 5
    if all([x < y for x, y in zip(arr, arr[1:])]):
        return 1
    if all([x <= y for x, y in zip(arr, arr[1:])]):
        return 2
    if all([x > y for x, y in zip(arr, arr[1:])]):
        return 3
    if all([x >= y for x, y in zip(arr, arr[1:])]):
        return 4
    return 0


def sequence_classifier2(arr):
    """Решение на уровне middle разработчика."""

    def get_sign(a, b):
        return -1 if a - b < 0 else 1 if a - b > 0 else 0

    signs = list(sorted(set(map(lambda a, b: get_sign(a, b), arr, arr[1:]))))
    mask = {
        "0": 5,
        "-1": 1,
        "-10": 2,
        "1": 3,
        "01": 4,
        "-101": 0,
        "-11": 0,
    }
    result = mask["".join((str(x) for x in signs))]
    return result


from functools import reduce


def sequence_classifier(arr):
    """Решение на уровне senior разработчика."""

    def get_sign(a, b):
        return -1 if a - b < 0 else 1 if a - b > 0 else 0

    mask = {
        5: 0,  # 0b101
        7: 0,  # 0b111
        1: 1,  # 0b1
        3: 2,  # 0b11
        4: 3,  # 0b100
        6: 4,  # 0b110
        2: 5,  # 0b10
    }

    signs = list(map(lambda a, b: 1 << (get_sign(a, b) + 1), arr, arr[1:]))
    acc = reduce(lambda acc, x: acc | x, signs, 0)

    return mask[acc]


# testing cases
print(sequence_classifier([3, 5, 8, 1, 14, 3]) == 0)
print(sequence_classifier([3, 5, 8, 9, 14, 23]) == 1)
print(sequence_classifier([3, 5, 8, 8, 14, 14]) == 2)
print(sequence_classifier([14, 9, 8, 5, 3, 1]) == 3)
print(sequence_classifier([14, 14, 8, 8, 5, 3]) == 4)
print(sequence_classifier([8, 8, 8, 8, 8, 8]) == 5)
print(sequence_classifier([8, 9]) == 1)
print(sequence_classifier([8, 8, 8, 8, 8, 9]) == 2)
print(sequence_classifier([9, 8]) == 3)
print(sequence_classifier([9, 9, 9, 8, 8, 8]) == 4)
print(sequence_classifier([3, 5, 8, 1, 14, 2]) == 0)
