def reverse_string(s):
    l = list(s)
    front = 0
    end = len(s) - 1
    while front < end:
        l[front], l[end] = l[end], l[front]
        front += 1
        end -= 1
    return "".join(l)

print(reverse_string("Hello World Hello"))
