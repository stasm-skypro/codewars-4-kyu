"""Python: your solution need to work with huge numbers (about a milion digits),
converting to int will not work."""


def sum_strings(x: str, y: str) -> str:
    # Equalize the lengths of the lists by adding leading zeros
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    # Perform addition digit by digit
    result = ""
    carry = 0
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        carry, remainder = divmod(digit_sum, 10)
        result = result + str(remainder)

    return ("1" * carry + result[::-1]).lstrip("0") or "0"


# test case
print(sum_strings("0", "0") == "0")
print(sum_strings("1", "1") == "2")
print(sum_strings("123", "456") == "579")
print(sum_strings("123456789", "456789") == "123913578")
