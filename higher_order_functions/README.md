# Chapter 19 (Python Higher-Order Functions)

### Task 1: Basic Higher-Order Function
#### Problem:
- Create a higher-order function `apply_function(func, value)` that:
    - Takes a function `func` and a value `value` as arguments.
    - Applies the function `func` to the value `value` and returns the result.
- Test `apply_function` by passing in a simple function like `lambda x: x * 3` and a value like `4`.

#### Example Output:
```
12
```

---

### Task 2: Function Returning a Function
#### Problem:
- Create a function `make_adder(add_value)` that returns a function `adder`:
    - The returned `adder` function takes a number and adds the `add_value` provided to `make_adder`.
- Use `make_adder` to create an incrementer function that increments a number by `1`. Test it on an input value.

#### Example Output:
```
6
```

---

### Task 3: Basic Decorator
#### Problem:
- Create a decorator `uppercase_decorator` that modifies the behavior of a function so that it always returns the result in uppercase.
- Apply `uppercase_decorator` to a function `greet()` that returns "Hello".

#### Example Output:
```
HELLO
```

---

### Task 4: Decorator with Arguments
#### Problem:
- Create a decorator `multiply_decorator` that takes a parameter `factor` and multiplies the return value of a function by that `factor`.
- Apply `multiply_decorator` to a function `get_price()` that returns a price (e.g., `50`).
- Call the decorated function with a factor of `2` and print the result.

#### Example Output:
```
100
```

---

### Task 5: Chaining Multiple Decorators
#### Problem:
- Create two decorators:
    - `double_decorator`: Doubles the result of the function it decorates.
    - `add_five_decorator`: Adds `5` to the result of the function it decorates.
- Apply both decorators to a function `get_value()` that returns `10`.
- Call the decorated function and print the result.

#### Example Output:
```
25
```

