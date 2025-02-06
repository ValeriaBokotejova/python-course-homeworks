int_list = [3, 7, 1, 9, 4]
print(int_list)

for i, num in enumerate(int_list):
    num = num * 3
    if num > 15:
        num = 'Too large'
    int_list[i] = num

print(int_list)
