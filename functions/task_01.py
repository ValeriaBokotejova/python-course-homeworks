def format_name(name, title="Mr./Ms."):
    first_name = name.split()[0].title()
    title = title.title() if title.endswith(".") else title.title() + "."
    return f"Title: {title}, Name: {first_name}"


name = input("Enter your name: ")
title = input("Enter your title: ")
print(format_name(name, title))
