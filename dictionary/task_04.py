phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

if phone_book["Alice"]:
    print(phone_book["Alice"])

del phone_book["Bob"]
print(phone_book)
