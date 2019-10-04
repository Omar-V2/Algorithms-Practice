def fib_r(n):
    if n < 2:
        return 1
    return fib_r(n-2) + fib_r(n-1)

def fib(n):
    i = 0
    j = 1
    for _ in range(n):
        j += i
        i = j - i
    return j

a = fib_r(35)
b = fib(35)
print(a, b)
print(a == b)
