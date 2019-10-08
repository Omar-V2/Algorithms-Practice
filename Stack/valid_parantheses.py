from stack import Stack

def valid_parantheses(expression):
    stack = Stack()
    pairs = {"(": ")", "[": "]", "{": "}"}
    for char in expression:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty() or pairs[stack.top()] != char:
                return False
            else:
                stack.pop()
    return stack.is_empty()

print(valid_parantheses("(a+b])"))


