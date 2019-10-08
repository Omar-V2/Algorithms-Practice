from stack import Stack

def eval_prefix(expression):
    stack = Stack()
    operands = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }
    i = len(expression) - 1
    while i >= 0:
        if expression[i] in operands:
            op_1 = int(stack.pop())
            op_2 = int(stack.pop())
            result = operands[expression[i]](op_1, op_2)
            stack.push(result)
        else:
            stack.push(int(expression[i]))
        print(stack.items)
        i -= 1
    return stack.top()

print(eval_prefix("-+*23*549"))