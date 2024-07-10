def is_palindrome(s):
    # Function to check if a string is a palindrome
    return s == s[::-1]

def reverse_content(input_file, output_file_reversed, output_file_palindromes):
    with open(input_file, 'r') as f:
        content = f.read().strip()  # Read and strip any trailing whitespace/newlines
    
    reversed_content = content[::-1]  # Reverse the content
    
    palindromes = []
    words = content.split()
    for word in words:
        if is_palindrome(word):
            palindromes.append(word)
    
    # Write reversed content to output file
    with open(output_file_reversed, 'w') as f_reversed:
        f_reversed.write(reversed_content)
    
    # Write palindromes to output file
    with open(output_file_palindromes, 'w') as f_palindromes:
        for palindrome in palindromes:
            f_palindromes.write(palindrome + '\n')

if __name__ == '__main__':
    input_file = 'input.txt'  # Replace with your input file name
    output_file_reversed = 'reversed.txt'  # Replace with your reversed content output file name
    output_file_palindromes = 'palindromes.txt'  # Replace with your palindromes output file name
    
    reverse_content(input_file, output_file_reversed, output_file_palindromes)
