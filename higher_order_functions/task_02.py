def make_adder(add_value):
    def adder(number):
        return number + add_value
    return adder

incrementer = make_adder(1)
print(incrementer(5))
