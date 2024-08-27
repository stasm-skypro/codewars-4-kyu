def solution(arr):
    intervals = []
    for a, b in zip(arr, arr[1:]):
        intervals.append(b - a)

    p = float("inf")
    pref = [p] + intervals
    suff = intervals + [p]
    diff = [max(a, b) for a, b in zip(pref, suff)]

    for i in range(len(arr)):
        if diff[i] == 1:
            arr[i] = "-"

    res = []
    for i in range(len(arr)):
        if arr[i] != "-":
            if arr[i - 1] == "-":
                res[-1] = res[-1] + str(arr[i])
            else:
                res.append(str(arr[i]))
        elif arr[i] == "-":
            if arr[i - 1] != "-":
                res[-1] = res[-1] + "-"

    res_string = ",".join(res)

    return res_string


print(
    solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
    == "-6,-3-1,3-5,7-11,14,15,17-20"
)

print(
    solution(
        [
            -10,
            -9,
            -8,
            -6,
            -3,
            -2,
            -1,
            0,
            1,
            3,
            4,
            5,
            7,
            8,
            9,
            10,
            11,
            14,
            15,
            17,
            18,
            19,
            20,
        ]
    )
    == "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
)

print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) == "-3--1,2,10,15,16,18-20")
