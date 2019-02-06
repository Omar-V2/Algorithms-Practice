from array_stack import Stack

def reverse_string(string):
    end = len(string)
    reverse = ""
    for _ in range(len(string)):
        reverse += string[end-1]
        end -= 1
    return reverse

def reverse_string_stack(string):
    reversed = ""
    myStack = Stack()
    for char in string:
        myStack.push(char)
    for char in string:
        reversed += myStack.pop()
    return reversed
        

print(reverse_string("hello"))
print(reverse_string_stack("hello"))

