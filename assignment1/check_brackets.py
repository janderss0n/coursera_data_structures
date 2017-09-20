# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def is_balanced(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))
            continue

        if next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack:
                return i + 1
            last_bracket = opening_brackets_stack.pop()
            if not last_bracket.Match(next):
                return i + 1
            continue

    return 'Success' if not opening_brackets_stack else (opening_brackets_stack.pop().position + 1)


if __name__ == "__main__":
    text = sys.stdin.read()
    print(is_balanced(text))
