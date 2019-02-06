from array_stack import Stack
import operator


def evaluate_postfix(expression): # postfix is same except we iterate over the string in reverse and the order of temp1, temp2 is also reversed
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = Stack()
    for i in expression:
        if i == '+' or i == '-' or i == '*' or i == '/':
            temp1 = stack.pop()
            temp2 = stack.pop()
            result = operations[i](temp2, temp1)
            stack.push(result)
        else:
            stack.push(int(i))
    return stack.top()

expression = '23*54*+9-'
print(evaluate_postfix(expression))

    