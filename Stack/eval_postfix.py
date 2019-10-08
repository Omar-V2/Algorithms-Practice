from stack import Stack

def eval_postfix(expression):
    stack = Stack()
    operands = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    for element in expression:
        if element in operands:
            op_2 = int(stack.pop())
            op_1 = int(stack.pop())
            result = operands[element](op_1, op_2)
            stack.push(result)
        else:
            stack.push(int(element))
    return stack.top()

print(eval_postfix('23*54*+9-'))

