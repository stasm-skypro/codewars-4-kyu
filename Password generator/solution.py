"""Description:
You need to write a password generator that meets the following criteria:
    6 - 20 characters long
    contains at least one lowercase letter
    contains at least one uppercase letter
    contains at least one number
    contains only alphanumeric characters (no special characters)
Return the random password as a string.
Note: "randomness" is checked by counting the characters used in the generated
passwords - all characters should have less than 50% occurance. Based on
extensive tests, the normal rate is around 35%.
"""

from random import randint


def password_gen():
    letters = "qwertyuiopasdfghjklzxcvbnm"
    digits = "0123456789"

    prefix = (
        letters[randint(0, 25)]
        + letters[randint(0, 25)].upper()
        + digits[randint(0, 9)]
    )
    password = prefix
    for _ in range(randint(3, 17)):
        password = (
            password + "".join([letters, letters.upper(), digits])[randint(0, 34)]
        )

    return password


def password_gen2():
    pass


# testing case
for _ in range(40):
    pwd = password_gen()
    lower = any(c.islower() for c in pwd)
    upper = any(c.isupper() for c in pwd)
    number = any(c.isdigit() for c in pwd)

    print(
        "%-20s | %s!"
        % (pwd, ["INVALID", "OK"][6 <= len(pwd) <= 20 and lower and upper and number])
    )
