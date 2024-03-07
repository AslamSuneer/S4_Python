def ver(s):
    if '@' not in s:
        return False

    lpart, dpart = s.split('@')

    if '.' not in dpart:
        return False

    if not lpart.isalnum() or not dpart.replace('.', '').isalnum():
        return False

    return True

x = input("Enter Email : ")
if ver(x):
    print("Valid Email")
else:
    print("Invalid Email")
    
