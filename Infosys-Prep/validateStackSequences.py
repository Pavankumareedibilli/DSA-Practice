def validateStackSequences(pushed:list,popped:list):
    stack=[]
    j = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j = j+1
    if stack:
        return False
    else:
        return True



pushed = [1,2,3,4,5]
popped = [4,5,3,3,1]

print(validateStackSequences(pushed, popped))