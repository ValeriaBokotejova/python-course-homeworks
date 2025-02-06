str_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(str_list)

reversed_str_list = str_list[::-1] # [begin:end:step]

for index, fruit in enumerate(reversed_str_list):
    print(f"Index {index}: {fruit}")
