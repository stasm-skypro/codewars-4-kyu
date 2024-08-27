"""Description:

Given an array (arr) as an argument complete the function countSmileys that
should return the total number of smiling faces.
Rules for a smiling face:
    Each smiley face must contain a valid pair of eyes. Eyes can be marked
    as : or ;
    A smiley face can have a nose but it does not have to. Valid characters for
    a nose are - or ~
    Every smiling face must have a smiling mouth that should be marked with
    either ) or D

No additional characters are allowed except for those mentioned.
Valid smiley face examples: :) :D ;-D :~)
Invalid smiley faces: ;( :> :} :]
Example
countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;
Note
In case of an empty array return 0. You will not be tested with invalid input
(input will always be an array). Order of the face (eyes, nose, mouth) elements
will always be the same.
"""


def count_smileys1(arr):
    """Решение в стиле junior разработчика."""
    valid_eyes = [":", ";"]
    valid_nose = ["-", "~"]
    valid_mouth = [")", "D"]

    c = 0
    for comb in arr:
        if len(comb) == 3:
            if (
                comb[0] in valid_eyes
                and comb[1] in valid_nose
                and comb[2] in valid_mouth
            ):
                c = c + 1
        if len(comb) == 2:
            if comb[0] in valid_eyes and comb[1] in valid_mouth:
                c = c + 1

    return c


def count_smileys2(arr):
    """Решение в стиле middle разработчика."""
    valid_eyes = [":", ";"]
    valid_nose = ["-", "~"]
    valid_mouth = [")", "D"]

    filtered = filter(
        lambda x: (
            x[0] in valid_eyes and x[1] in valid_nose and x[2] in valid_mouth
            if len(x) == 3
            else x[0] in valid_eyes and x[1] in valid_mouth if len(x) == 2 else None
        ),
        arr,
    )
    c = len(list(filtered))
    return c


import re


def count_smileys(arr):
    regex = r"^[:;][-~]?[)D]$"
    result = [face for face in arr if re.match(regex, face)]

    return len(result)


# testing case
print(count_smileys([]) == 0)
print(count_smileys([":D", ":~)", ";~D", ":)"]) == 4)
print(count_smileys([":)", ":(", ":D", ":O", ":;"]) == 2)
print(count_smileys([";]", ":[", ";*", ":$", ";-D"]) == 1)

print(count_smileys([";o(", ";(", ";-D", ":oD", ":-D", ";(", ";oD"]) == 2)
