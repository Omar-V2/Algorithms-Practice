def product_array(array):
    zero_count = 0
    total_product = 1
    solution = []
    for i in array:
        if i == 0:
            zero_count += 1
        else:
            total_product *= i
    if zero_count > 1:
        return [0]*len(array)
    for i in array:
        if i == 0:
            solution.append(total_product)
        else:
            solution.append(total_product/i)
    return solution


a = [5, 4, 1, 2, 3]
print(product_array(a))

        