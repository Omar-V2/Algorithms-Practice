def sort_word_num(a):
    solution = []
    words = [i for i in a if type(i) == str]
    numbers = [i for i in a if type(i) == int]
    words.sort()
    numbers.sort()
    num_idx = 0
    word_idx = 0
    for i in a:
        if type(i) == str:
            solution.append(words[word_idx])
            word_idx += 1
        else:
            solution.append(numbers[num_idx])
            num_idx += 1
    return solution

print(sort_word_num(['car', 'truck', 8, 4, 'bus', 6, 1]))