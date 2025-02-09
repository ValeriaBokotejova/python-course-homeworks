def min_max_avg(numbers):
    if not numbers:
        return None, None, None
    
    min_num = min(numbers)
    max_num = max(numbers)
    average = sum(numbers) / len(numbers)

    return min_num, max_num, average


list_of_num = [5, 10, 3]
min_num, max_num, average = min_max_avg(list_of_num)

print(f"Min: {min_num}, Max: {max_num}, Average: {average}")
