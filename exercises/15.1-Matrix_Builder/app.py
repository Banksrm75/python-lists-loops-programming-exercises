# Your code here
def matrix_builder(int):
    matrix = [] 

    for i in range(int):
        row = []
        for j in range(int):
            row.append(1)
        matrix.append(row)

    return matrix

result = matrix_builder(3)

print(result)

