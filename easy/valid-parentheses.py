class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == '{' and char != '}':
                    return False
                if top == '(' and char != ')':
                    return False
                if top == '[' and char != ']':
                    return False
        return len(stack) == 0