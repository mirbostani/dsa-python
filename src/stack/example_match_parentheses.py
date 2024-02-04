def is_parentheses_matched(expression: str) -> bool:
    stack: list[str] = []
    opening_brackets: set[str] = {"(", "[", "{"}
    closing_brackets_mapping: dict[str, str] = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets_mapping:
            if not stack or stack.pop() != closing_brackets_mapping.get(char, None):
                return False
            
    return not stack # The expression is balanced if the stack is empty


if __name__ == "__main__":
    expression1: str = "{([[]])}"
    is_balanced = is_parentheses_matched(expression1)
    print(is_balanced) # True

    expression2: str = "{([[]))}"
    is_balanced = is_parentheses_matched(expression2)
    print(is_balanced) # False

    expression3: str = "(*[])"
    is_balanced = is_parentheses_matched(expression3)
    print(is_balanced) # True