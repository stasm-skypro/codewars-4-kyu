"""Python: your solution need to work with huge numbers (about a milion digits),
converting to int will not work."""


def sum_strings(x: str, y: str) -> str:
    if x in ["", "0"] and y in ["", "0"]:
        return "0"

    # Convert input strings to lists of digits
    listx = list(x)
    listy = list(y)

    # Equalize the lengths of the lists by adding leading zeros
    while len(listx) < len(listy):
        listx.insert(0, "0")
    while len(listy) < len(listx):
        listy.insert(0, "0")

    # Perform addition digit by digit
    result = []
    carry = 0
    for i in range(len(listx) - 1, -1, -1):
        digit_sum = int(listx[i]) + int(listy[i]) + carry
        carry, remainder = divmod(digit_sum, 10)
        result.insert(0, str(remainder))

    # Add any remaining carry
    if carry:
        result.insert(0, str(carry))

    # Remove leading zeros
    while result[0] == "0":
        result.remove(result[0])

    # Convert the list back to a string
    return "".join(result)


# test case
print(sum_strings("0", "0") == "0")
print(sum_strings("1", "1") == "2")
print(sum_strings("123", "456") == "579")
print(sum_strings("123456789", "456789") == "123913578")
