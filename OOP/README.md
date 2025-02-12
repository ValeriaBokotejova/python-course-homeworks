# Chapter 16: Python OOP

## Task 1: Basic Class and Object Creation
**Problem:**
Create a class Car with the following attributes (Use the  `__init__` method):
- `make` (string)
- `model` (string)
- `year` (integer)
Create an instance of the class with values for `make`, `model`, and `year`.
Print the instance's attributes.
#### Example Output:
```python
Make: Toyota
Model: Camry
Year: 2020
```
___
## Task 2: Constructor Method(`__init__`)
**Problem:**
Create a class Rectangle with the following attributes:
- `width` (integer)
- `height` (integer)
Use the `__init__` method to initialize the attributes when an object is created.
Create an instance of `Rectangle` and print its `width` and `height`.
#### Example Output:
```python
Width: 5
Height: 10
```
___
## Task 3: Instance Method
**Problem:**
- Modify the `Rectangle` class from Task 2 to include a method `area()` that calculates and returns the area of the rectangle `(width * height)`.
- Create an instance and call the `area()` method to get the rectangle's area.
#### Example Output:
```python
Area: 50
```
___
## Task 4: Inheritance
**Problem:**
- Create a class `Vehicle` with the attributes `make`, `model`, and `year`.
- Create a subclass `ElectricCar` that inherits from `Vehicle` and adds the attribute `battery_size` (integer).
- Create an instance of `ElectricCar`, and print the attributes from both `Vehicle` and `ElectricCar`.
#### Example Output:
```python
Make: Tesla
Model: Model S
Year: 2022
Battery Size: 100
```
___
## Task 5: Method Overriding
**Problem:**
- In Task 4, override the `__init__` method of `ElectricCar` to initialize both the attributes of `Vehicle` and `ElectricCar` (using `super()`).
Call the `__init__` method from `ElectricCar` and print the values of all attributes.
#### Example Output:
```python
Make: Tesla
Model: Model X
Year: 2023
Battery Size: 120
```
___
## Task 6: Dunder Method(`__str__`)
**Problem:**
- Create a class `Book` with attributes `title`, `author`, and `year_published`.
- Override the `__str__()` method to return a string in the format:
```"[Title] by [Author] (Published: [Year])"```
- Create an instance of Book and print it to see the custom string representation.
#### Example Output:
```python
The Great Gatsby by F. Scott Fitzgerald (Published: 1925)
```
___
## Task 7: Dunder Method(`__eq__`)
**Problem:**
- Create a class `Person` with attributes `name` and `age`.
- Override the `__eq__()` method to compare two `Person` objects based on their `name` and `age`.
- Create two instances of `Person` and check if they are equal using the `==` operator.
#### Example Output:
```python
Are they equal? True
```
___
## Task 8: Class Method and Static Method
**Problem:**
- Create a class `Employee` with the following:
    - `name` (string)
    - `salary` (float)
- Add a class method `from_string()` that creates an `Employee` instance from a string in the format ```"name, salary"```.
- Add a static method ```is_high_salary()``` that checks if an employee's salary is above 100,000.
- Demonstrate creating an employee from a string and checking their salary.
#### Example Output:
```python
Employee name: Alice, Salary: 120000
Is the salary high? True
```
___
## Bonus Task 9: Create a Custom Iterator for a Fibonacci Sequence
**Problem:**
Create a custom iterator class called `FibonacciIterator` that generates numbers in the Fibonacci sequence. The iterator should take an input `n`, which specifies the maximum number of Fibonacci numbers to generate.
- Implement the `__iter__` and `__next__` methods to make the class an iterator.
- Use the iterator to generate and print the Fibonacci sequence up to `n` terms.
#### Example Input:
```python
fib = FibonacciIterator(5)
for num in fib:
    print(num)
```
#### Expected Output:
```python
0
1
1
2
3
```
### Challenge:
- Extend the iterator to raise a `StopIteration` exception when the maximum `n` is reached.
- Use the iterator with the `list()` function, e.g., ```list(FibonacciIterator(7))``` should output ```[0, 1, 1, 2, 3, 5, 8]```

___

These tasks cover a range of OOP principles from **basic classes and objects** to advanced techniques like **method overriding, dunder methods, inheritance**, and **class/static methods**.

