def is_balanced(s: str) -> bool:
    stack = []
    open_brackets = {'(', '[', '{'}
    closed_brackets = {')', ']', '}'}
    open_to_closed = {'(': ')', '[': ']', '{': '}'}
    for i in s:
        print(stack)
        if i in open_brackets:
            stack.append(i)
        elif i in closed_brackets:
            if not stack or stack and open_to_closed[stack.pop()] != i:
                return False
    return stack == []

print(is_balanced(s))