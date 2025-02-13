def multiply_decorator(factor):
    def decorator(func):
        def wrap():
            return func() * factor
        return wrap
    return decorator

@multiply_decorator(2)
def get_price():
    return 50

print(get_price())
