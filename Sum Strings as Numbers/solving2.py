"""Python: your solution need to work with huge numbers (about a milion digits),
converting to int will not work."""


def sum_strings(x: str, y: str) -> str:
    if x in ["", "0"] and y in ["", "0"]:
        return "0"

    # Equalize the lengths of the lists by adding leading zeros
    while len(x) < len(y):
        x = "0" + x
    while len(y) < len(x):
        y = "0" + y

    # Perform addition digit by digit
    result = ""
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        digit_sum = int(x[i]) + int(y[i]) + carry
        carry, remainder = divmod(digit_sum, 10)
        result = str(remainder) + result

    # Add any remaining carry
    if carry:
        result = str(carry) + result

    # Remove leading zeros
    while result[0] == "0":
        result = result[1:]

    # Convert the list back to a string
    return result


# test case
print(sum_strings("0", "0") == "0")
print(sum_strings("1", "1") == "2")
print(sum_strings("123", "456") == "579")
print(sum_strings("123456789", "456789") == "123913578")
