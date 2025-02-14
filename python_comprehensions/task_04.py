lists = [[1, 2, 3], [4, 5], [6, 7]]
flat_list = [num for sub in lists for num in sub]
print(flat_list)
