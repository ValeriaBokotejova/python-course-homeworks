str_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(str_list)

reversed_str_list = []
for i in range(len(str_list) - 1, -1, -1):  
    reversed_str_list.append(str_list[i])

for index, fruit in enumerate(reversed_str_list):
    print(f"Index {index}: {fruit}")
