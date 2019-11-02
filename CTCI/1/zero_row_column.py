def zero_row_column(m):
    columns = {}
    rows = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                rows[i] = 1
                columns[j] = 1
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i in rows or j in columns:
                m[i][j] = 0
    return m

m = [
    [1, 0, 4, 6],
    [0, 2, 3, 8],
    [7, 8, 9, 2],
    [2, 4, 7, 8]
]

m2 = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
print(zero_row_column(m2))