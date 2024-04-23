import matplotlib.pyplot as plt

# Function to read values from a file
def read_values_from_file(filename):
    values = []
    with open(filename, 'r') as file:
        for line in file:
            value = float(line.strip())  # Assuming each line contains a numerical value
            values.append(value)
    return values

# Read values from a file (replace 'filename.txt' with your actual file name)
filename = 'filename.txt'
values = read_values_from_file(filename)

# Plotting the bar chart
plt.bar(range(len(values)), values)
plt.xlabel('Data Points')
plt.ylabel('Values')
plt.title('Bar Chart of Values from File')
plt.show()
