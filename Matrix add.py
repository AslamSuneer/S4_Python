def input_matrix(r, c):
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input("Enter Element : ")))
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

def add_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

while True:
    print("\n1. Input Matrices\n2. Display Matrices\n3. Add Matrices\n4. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        rows = int(input("Enter Number of Rows: "))
        cols = int(input("Enter Number of Columns: "))
        print("Enter Matrix A:")
        matrix_a = input_matrix(rows, cols)
        print("Enter Matrix B:")
        matrix_b = input_matrix(rows, cols)
    elif choice == 2:
        print("Matrix A:")
        display_matrix(matrix_a)
        print("\nMatrix B:")
        display_matrix(matrix_b)
    elif choice == 3:
        result = add_matrices(matrix_a, matrix_b)
        print("Resultant Matrix:")
        display_matrix(result)
    elif choice == 4:
        break
    else:
        print("Invalid Choice. Please choose again.")
      
