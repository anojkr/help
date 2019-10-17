def isBalanced(s):

    A= list(s)
    stack = [-1]
    for i in range(0, len(A)):
        if A[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif A[i] == ']' and stack[-1] == '[':
            stack.pop()
        elif A[i] == '}' and stack[-1] == '{':
            stack.pop()
        else:
            stack.append(A[i])
    if len(stack) >1:
        return 'NO'
    return 'YES'