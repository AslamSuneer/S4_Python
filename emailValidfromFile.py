import re

def is_valid_email(email):
    # Regular expression pattern for basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def validate_emails_from_file(file_name):
    with open(file_name, 'r') as f:
        emails = f.readlines()
    
    for email in emails:
        email = email.strip()  # Remove any surrounding whitespace or newline characters
        if is_valid_email(email):
            print(f'{email}: valid')
        else:
            print(f'{email}: invalid')

if __name__ == '__main__':
    input_file = 'emails.txt'  # Replace with your input file name
    validate_emails_from_file(input_file)
