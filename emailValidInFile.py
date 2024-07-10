import re

def is_valid_email(email):
    # Regular expression pattern for basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def main():
    input_file = 'emails.txt'       # Replace with your input file name
    output_file = 'valid_emails.txt'  # Replace with your output file name
    
    with open(input_file, 'r') as f:
        emails = f.readlines()
    
    with open(output_file, 'w') as f:
        for email in emails:
            email = email.strip()  # Remove any surrounding whitespace or newline characters
            if is_valid_email(email):
                f.write(f'{email}: valid\n')
            else:
                f.write(f'{email}: invalid\n')

if __name__ == '__main__':
    main()
