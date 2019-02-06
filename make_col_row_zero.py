def make_zero(M):
    R = [0 for i in range(len(M))]
    C = [0 for i in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 0:
                C[j] = 1
                R[i] = 1
    for i in range(len(M)):
        for j in range(len(M[i])):
            if C[i] == 0:
                M[i][j] = 0
    return M


M = [[1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1]]

print(make_zero(M))