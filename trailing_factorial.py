def factorial(n, cache):
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return 1
    cache[n] = n * factorial(n-1, cache)
    return cache[n]

def trailing_zeros(n):
    count = 0
    i = 5
    while (n / i) >= 1:
        count += n // i
        i *= 5
    return count

print(trailing_zeros(4617))
# cache = {}
# print(factorial(20, cache))
# print(factorial(30, cache))


