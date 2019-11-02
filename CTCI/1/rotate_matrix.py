def rotate_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i < j:
                m[i][j], m[j][i] = m[j][i], m[i][j]
    for row in m:
        row.reverse()
    return m


m = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

rotated = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
print(rotate_matrix(m))