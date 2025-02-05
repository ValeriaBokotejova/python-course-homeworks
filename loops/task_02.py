int_list = [10, 20, 30, 40, 50, 11, 17, 22]
print(int_list)

even_sum = 0
even_count = 0

for num in int_list:
    if num % 2 == 0:
        even_sum += num
        even_count += 1

print(f"Sum of even numbers: {even_sum}")
print(f"Number of even numbers: {even_count}")
