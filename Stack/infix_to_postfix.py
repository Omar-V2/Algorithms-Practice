from stack import Stack

def infix_to_postfix(infix):
    stack = Stack()
    postfix = ""
    operators = {"+": "* / -", "-": "* / +", "*": "/", "/": "*"}
    for element in infix:
        if element == "(":
            stack.push(element)
        elif element == ")":
            while not stack.is_empty() and stack.top() != "(":
                postfix += stack.pop()
            stack.pop()
        elif element in operators:
            # pop all operators with greater precedence
            while not stack.is_empty() and stack.top() != "(" and stack.top() in operators[element]:
                postfix += stack.pop()
            stack.push(element)
        else:
            postfix += element
    while not stack.is_empty():
        postfix += stack.pop()
    return postfix

print(infix_to_postfix("((A+B)*C-D)*E"))
