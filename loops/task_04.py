matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    row_values = []
    row_sum = 0
    for num in row:
        row_values.append(num)
        row_sum += num

    print(f"Row: {row_values} Sum: {row_sum}")
