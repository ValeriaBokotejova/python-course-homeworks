int_list = [5, 12, 7, 9, 20, 15]
print(f"Original list: {int_list}")

int_list.append(25)
print(f"After adding 25: {int_list}")

int_list.remove(7)
print(f"After removing 7: {int_list}")

int_list.sort()
print(f"Sorted list: {int_list}")

print(f"Largest number: {max(int_list)}")

print(f"Smallest number: {min(int_list)}")
