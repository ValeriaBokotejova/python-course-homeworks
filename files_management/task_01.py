def write_user_info_to_file():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    favorite_color = input("Enter your favorite color: ")

    with open("user_info.txt", "w") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Age: {age}\n")
        file.write(f"Favorite Color: {favorite_color}\n")

    print("User information has been written to user_info.txt")

write_user_info_to_file()
