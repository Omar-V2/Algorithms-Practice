from time import time
cache = {}
def fib(n):
    if n == 1 or n == 2:
        return 1
    if n in cache:
        return cache[n]
    else:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

def fib_bottom_up(n):
    if n == 0  or n == 1:
        return 1
    bottum_up_arr = [None]*(n+1)
    bottum_up_arr[0] = 1
    bottum_up_arr[1] = 1
    for i in range(2, n+1):
        bottum_up_arr[i] = bottum_up_arr[i-1] + bottum_up_arr[i-2]
    return bottum_up_arr[n]

start = time()
for i in range(6):
    print(fib_bottom_up(i))
end = time()
print(end - start)