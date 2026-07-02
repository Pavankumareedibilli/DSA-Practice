def reverse_stack(stack:list):
    if not stack:
        return
    temp = stack.pop()
    reverse_stack(stack)
    add_at_end(stack,temp)

def add_at_end(stack,val):
    if not stack:
        stack.append(val)
        return
    temp = stack.pop()
    add_at_end(stack,val)
    stack.append(temp)

stack=[1,2,3,4]
reverse_stack(stack)
print(stack)

