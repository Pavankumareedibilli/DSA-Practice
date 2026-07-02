def sort_stack(stack):
    if not stack:
        return
    
    temp = stack.pop()

    sort_stack(stack)

    insert(stack,temp)

def insert(stack,val):
    if not stack or val > stack[-1]:
        stack.append(val)
        return 
    
    temp = stack.pop()

    insert(stack,val)

    stack.append(temp)


stack = [3,4,1,2]
sort_stack(stack)
print(stack)
