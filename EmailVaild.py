def verify_email(email):
    if '@' not in email or '.' not in email[email.index('@'):]:
        return False
    if not email[email.index('@')+1:email[email.index('@'):].index('.')].isalpha():
        return False
    if not email[email[email.index('@'):].index('.')+1:].isalpha():
        return False
    return True

email_input = input("Enter Email: ")
if verify_email(email_input):
    print("Valid Email")
else:
    print("Invalid Email")
  
