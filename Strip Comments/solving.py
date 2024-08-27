"""Complete the solution so that it strips all text that follows any of a set
of comment markers passed in. Any whitespace at the end of the line should also
be stripped out.
Example:
Given an input string of:
apples, pears # and bananas
grapes
bananas !apples
The output expected would be:
apples, pears
grapes
bananas
The code would be called like so:
result = strip_comments("apples, pears # and bananas\n
                         grapes\n
                         bananas !apples", ["#", "!"])
# result should == "apples, pears\n
                    grapes\n
                    bananas"""


def strip_comments(strng, markers):
    strng_list = strng.split("\n")
    new_strng_list = []
    for word in strng_list:
        new_word = ""
        for char in word:
            if char in markers:
                break
            else:
                new_word = new_word + char
        new_strng_list.append(new_word.rstrip())

    result = "\n".join(new_strng_list)

    return result


# testing cases
print(
    strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    == "apples, pears\ngrapes\nbananas"
)
print(strip_comments("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd")
print(strip_comments(" a #b\nc\nd $e f g", ["#", "$"]) == " a\nc\nd")
