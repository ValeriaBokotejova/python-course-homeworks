def double_decorator(func):
    def wrap():
        return func() * 2
    return wrap

def add_five_decorator(func):
    def wrap():
        return func() + 5
    return wrap

@add_five_decorator
@double_decorator
def get_value():
    return 10

print(get_value())
