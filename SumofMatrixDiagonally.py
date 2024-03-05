def disp(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def input_matrix(size):
    matrix = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(int(input("Enter Element: ")))
        matrix.append(row)
    return matrix

size = int(input("Enter Number of rows and Columns: "))
print("Input elements for Matrix A:")
matrix_a = input_matrix(size)
matrix_b = []

print("\nMatrix A:")
disp(matrix_a)

print("\nMatrix B:")
# Calculate the sum along the main diagonal
diagonal_sum = sum(matrix_a[i][i] for i in range(size))
for row in matrix_a:
    matrix_b.append(row + [sum(row)])
matrix_b.append([sum(col) for col in zip(*matrix_a)] + [diagonal_sum])

disp(matrix_b)
