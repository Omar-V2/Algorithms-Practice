def str_to_int(s):
    pwr_index = len(s) - 1
    num = lambda x: ord(x) - ord('0')
    value = 0
    for char in s:
        n = num(char) * (10**pwr_index)
        value += n
        pwr_index -= 1
    return value

print(str_to_int('546'))