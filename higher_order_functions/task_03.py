def uppercase_decorator(func):
    def wrap():
        result = func()
        return result.upper()
    return wrap

@uppercase_decorator
def greet():
    return "Hello"

print(greet())
