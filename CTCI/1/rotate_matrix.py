def rotate_matrix(m):
    rows = len(m)
    columns = len(m[0])
    rotated_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            pass

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate_matrix(m))