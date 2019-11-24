def is_balanced(s: str) -> bool:
    stack = []
    open_brackets = {'(', '[', '{'}
    closed_brackets = {')', ']', '}'}
    open_to_closed = {'(': ')', '[': ']', '{': '}'}
    for bracket in s:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in closed_brackets:
            if not stack or stack and open_to_closed[stack.pop()] != bracket:
                return False
    return stack == []

print(is_balanced(s))
