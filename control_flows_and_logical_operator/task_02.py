password = str(input("Enter password: "))

match password:
    case p if len(p) < 8:
        print("Password is invalid. Reason: At least 8 characters long.")
    case p if " " in p:
        print("Password is invalid. Contains spaces.")
    case p if "Python" not in p :
        print("Password is invalid. Does not contain the word 'Python'.")
    case _:
        print("Password is valid.")
