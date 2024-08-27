def solution(string, markers):
    parts = string.split("\n")
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return "\n".join(parts)


# testing cases
print(
    solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    == "apples, pears\ngrapes\nbananas"
)
print(solution("a #b\nc\nd $e f g", ["#", "$"]) == "a\nc\nd")
print(solution(" a #b\nc\nd $e f g", ["#", "$"]) == " a\nc\nd")
