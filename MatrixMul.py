# Function to multiply two matrices
def matrix_multiply(A, B):
    # Get the dimensions of the matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if the matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Cannot multiply matrices: The number of columns in A must be equal to the number of rows in B.")

    # Create the result matrix and initialize it with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform the multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Example matrices
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Multiply the matrices
result = matrix_multiply(A, B)

# Print the result
for row in result:
    print(row)
  
