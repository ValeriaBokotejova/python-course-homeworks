password = str(input("Enter password: "))

if len(password) < 8:
    print("Password is invalid. Reason: At least 8 characters long.")
elif " " in password:
    print("Password is invalid. Contains spaces.")
elif "Python" not in password:
    print("Password is invalid. Does not contain the word 'Python'.")
else:
    print("Password is valid.")
