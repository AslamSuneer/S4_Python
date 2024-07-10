def matrix_multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if matrices can be multiplied
    if cols_A != rows_B:
        print("Cannot multiply matrices. Number of columns in A must be equal to number of rows in B.")
        return None

    # Result matrix C with dimensions rows_A x cols_B
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Function to input a matrix from user
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter {rows}x{cols} matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"Enter element [{i+1},{j+1}]: ")))
        matrix.append(row)
    return matrix

# Main program
if __name__ == "__main__":
    # Input dimensions of matrices
    rows_A = int(input("Enter number of rows for matrix A: "))
    cols_A = int(input("Enter number of columns for matrix A: "))
    rows_B = int(input("Enter number of rows for matrix B: "))
    cols_B = int(input("Enter number of columns for matrix B: "))

    if cols_A != rows_B:
        print("Matrix multiplication not possible. Number of columns in A must be equal to number of rows in B.")
    else:
        # Input matrices A and B
        A = input_matrix(rows_A, cols_A)
        B = input_matrix(rows_B, cols_B)

        # Perform multiplication
        result = matrix_multiplication(A, B)

        # Print result
        if result:
            print("Result of matrix multiplication:")
            for row in result:
                print(row)
              
