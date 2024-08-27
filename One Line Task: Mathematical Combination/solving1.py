# from functools import reduce

# def comb(n, k):
#     numerator = reduce(lambda a, b: a * b, [x for x in range(n, n - k, -1)], 1)
#     denomunator = reduce(lambda a, b: a * b, [x for x in range(k, 0, -1)], 1)
#     result = numerator / denomunator

#     return result


# comb = lambda n, k: reduce(
#     lambda a, b: a * b, [x for x in range(n, n - k, -1)], 1
# ) / reduce(lambda a, b: a * b, [x for x in range(k, 0, -1)], 1)


# def comb(n, k):
#     numerators = [a for a in range(n, n - k, -1)]
#     denominators = [b for b in range(1, k + 1, 1)]

#     result = 1
#     for a, b in zip(numerators, denominators):
#         fract = a / b
#         result = result * fract

#     return result


# def fac(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fac(n - 1) * n


# def comb(n, k):
#     if k == 0 or n == k:
#         return 1
#     elif k > n:
#         return 0
#     else:
#         return fac(n) / (fac(k) * fac(n - k))


# def fac(x):
#     res = 1
#     for i in range(1, x + 1):
#         res = res * i
#     return res

# f = lambda x: 0**x or x * f(x - 1)
# comb = lambda n, k: 1 if k in [0, n] else 0 if k > n else f(n) // (f(k) * f(n - k))

# Решение из https://codegolf.stackexchange.com/questions/1744/mathematical-combination
# n, k = int(input()), int(input())
# f = lambda x: +(x < 2) or x * f(x - 1)
# print(f(n) // (f(k) * f(n - k)))

# f = lambda x: +(x < 2) or x * f(x - 1)
# comb = lambda n, k: (f(n) // (f(k) * f(n - k)))

comb = lambda n, k: (b := 2 << n | 1) ** n >> n * k + k & b - 2

# test case
print(comb(52, 5) == 2598960)

print(comb(1, 0) == 1)
print(comb(1, 1) == 1)
print(comb(1, 2) == 0)

print(comb(6, 3) == 20)
print(comb(6, 4) == 15)
print(comb(6, 9) == 0)
