# Chapter 4: Python Lists and Tuples

## Task 1: Random Team Picker
### Problem:
- Create a list of names (e.g., your classmates or colleagues).
- Use `random.choice()` to randomly select one name to lead a group project.
- Print the selected name.

### Example Output:
```
Participants: ['Alice', 'Bob', 'Charlie', 'Diana']
Selected leader: Charlie
```

---

## Task 2: Random Password Generator
### Problem:
- Create a list of characters containing:
  - All lowercase letters ('a' to 'z').
  - All uppercase letters ('A' to 'Z').
  - Digits ('0' to '9').
- Use `random.choices()` to generate a random 8-character password.
- Print the generated password.

### Example Output:
```
Generated password: X7gK2aLp
```

---

## Task 3: List Operations
### Problem:
- Create a list of integers: `[5, 12, 7, 9, 20, 15]`.
- Perform and print the following operations:
  1. Add a new number `25` to the list.
  2. Remove the number `7` from the list.
  3. Sort the list in ascending order.
  4. Find and print the largest and smallest numbers in the list.

### Example Output:
```
Original list: [5, 12, 7, 9, 20, 15]
After adding 25: [5, 12, 7, 9, 20, 15, 25]
After removing 7: [5, 12, 9, 20, 15, 25]
Sorted list: [5, 9, 12, 15, 20, 25]
Largest number: 25
Smallest number: 5
```

---

## Task 4: List Indexing and Slicing
### Problem:
- Create a list of 7 days of the week: `['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']`.
- Perform the following tasks:
  1. Print the first day of the week.
  2. Print the last day of the week.
  3. Print the middle days (Tuesday to Saturday).
  4. Replace 'Wednesday' with 'Humpday' and print the updated list.

### Example Output:
```
First day: Monday
Last day: Sunday
Middle days: ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
Updated list: ['Monday', 'Tuesday', 'Humpday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
```

---

## Learn the Difference Between List and Tuple in Python

---

## Task 5: Swap Values Using Tuples
### Problem:
- Write a program that swaps the values of two variables using tuples.
- Prompt the user to input two values.
- Use a tuple to perform the swap in a single line of code.
- Display the values before and after the swap.

### Example Input:
```
Enter first value: 10  
Enter second value: 20
```

### Expected Output:
```
Before Swap: First Value = 10, Second Value = 20  
After Swap: First Value = 20, Second Value = 10
```

### Solutions:
1. Using Python swap method (easy and correct).
2. Using arithmetic method (advanced but complicated).

---

## Task 6: Unpack Tuples with Mixed Data
### Problem:
- Given a tuple containing mixed data types, write a program to unpack its values into variables and display their types.
- Define a tuple with at least one integer, one float, one string, and one boolean.
- Unpack the tuple into individual variables.
- Print each value and its corresponding type.

### Example Input:
```
data = (42, 3.14, "Hello", True)
```

### Expected Output:
```
Integer: 42 (Type: <class 'int'>)  
Float: 3.14 (Type: <class 'float'>)  
String: Hello (Type: <class 'str'>)  
Boolean: True (Type: <class 'bool'>)
```
