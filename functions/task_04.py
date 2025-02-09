def create_user(username, email, password, **kwargs):
    if len(username) < 5:
        return "Error: Username must be at least 5 characters long."
    if "@" not in email:
        return "Error: Email must contain '@'."
    if len(password) < 8:
        return "Error: Password must be at least 8 characters long."
    
    user_data = {
        "username": username,
        "email": email,
        "password": password
    }

    user_data.update(kwargs)
    return user_data

valid_user = create_user("john123", "john@example.com", "securePass123", age=30)
invalid_user = create_user("ar", "ar.com", "1122")

print(valid_user)
print(invalid_user)
