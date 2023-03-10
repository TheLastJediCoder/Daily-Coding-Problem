"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets
are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

opposite_bracket_map = {"(": ")", "{": "}", "[": "]"}


def check_if_brackets_are_balanced(string: str) -> bool:
    stack: list[str] = []
    for s in string:
        if len(stack) > 0 and opposite_bracket_map.get(stack[-1]) == s:
            stack.pop()
        else:
            stack.append(s)
    return len(stack) == 0


print(check_if_brackets_are_balanced("([])[]({})"))
print(check_if_brackets_are_balanced("([)]"))
print(check_if_brackets_are_balanced("((()"))
