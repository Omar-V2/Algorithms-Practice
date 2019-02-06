from array_stack import Stack

def isBalanced(expression):
    stack = Stack()
    opening = ["(", "[", "{"]
    closing = [")", "]", "}"]
    for char in expression:
        if char == "(" or char == "[" or char == "{":
            stack.push(char)
        else:
            if stack.isEmpty() or closing.index(char) != opening.index(stack.top()): # check if parantheses are of same type:
                return False
            else:
                stack.pop()
    return stack.isEmpty()

def st(s):
    while '()' in s or '{}' in s or '[]' in s:
        print(s)
        s = s.replace('{}','').replace('()','').replace('[]','')
        return len(s)

print(isBalanced("(())"))
# print(st("(())"))