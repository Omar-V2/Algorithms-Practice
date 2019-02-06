from array_stack import Stack  


def balance(s):
    stack = Stack()
    ans = s
    for i in s:
        if i == ")":
            if stack.isEmpty():
                ans = "(" + ans
            else:
                stack.pop()
        else:
            stack.push(i)
    ans += len(stack.items)*")"
    return ans

print(balance("))))("))