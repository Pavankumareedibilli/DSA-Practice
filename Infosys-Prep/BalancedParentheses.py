def BalancedParentheses(s:str):
    stack = []
    pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in '}])':
            if not stack or stack.pop()!= pairs[ch]:
                return False
    return len(stack)==0


print(BalancedParentheses("()"))        # True
print(BalancedParentheses("()[]{}"))    # True
print(BalancedParentheses("(]"))        # False
print(BalancedParentheses("([{}])"))    # True
print(BalancedParentheses("((("))       # False