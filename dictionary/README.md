# Chapter 9: Python Dictionary

## Overview
This chapter covers fundamental dictionary operations in Python. The tasks will help you practice creating, updating, iterating through, and managing dictionaries effectively.

---

## Task 1: Basic Dictionary Operations
- Create a dictionary representing a person's details.
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
```
- Update the "city" field to "San Francisco".
- Add a new key-value pair "job": "Engineer".
- Print the updated dictionary.

### Expected Output:
```python
{'name': 'Alice', 'age': 25, 'city': 'San Francisco', 'job': 'Engineer'}
```

---

## Task 2: Dictionary Iteration
- Create a dictionary with student names as keys and their grades as values.
```python
grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "Diana": 95,
    "Eve": 78
}
```
- Use a `for` loop to iterate through the dictionary and print each student's name and their grade.

### Expected Output:
```python
Alice: 85
Bob: 92
Charlie: 88
Diana: 95
Eve: 78
```

---

## Task 3: Dictionary with Nested Data
- Create a dictionary representing a collection of books.
- Each book should have a title, author, and publication year.
```python
books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}
```
- Use a `for` loop to iterate through the outer dictionary.
- For each book, print the title, author, and year.

### Expected Output:
```python
Book: 1984, Author: George Orwell, Year: 1949
Book: To Kill a Mockingbird, Author: Harper Lee, Year: 1960
```

---

## Task 4: Dictionary Search and Deletion
- Create a phone book dictionary.
```python
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}
```
- Check if `"Alice"` exists and print her phone number.
- Delete `"Bob"` from the dictionary using `del`.
- Print the updated dictionary.

### Expected Output:
```python
Alice's phone number: 123-456-7890
{'Alice': '123-456-7890', 'Charlie': '555-123-4567'}
```
