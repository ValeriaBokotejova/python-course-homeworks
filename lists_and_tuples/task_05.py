first_value = input("Enter first value: ")
second_value = input("Enter second value: ")

print(f"Before Swap: First Value = {first_value}, Second Value = {second_value}")

first_value, second_value = second_value, first_value

print(f"After Swap: First Value = {first_value}, Second Value = {second_value}")
