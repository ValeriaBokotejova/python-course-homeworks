numbers = [2, 4, 6, 8, 10]

doubled = map(lambda x: x * 2, numbers)

filtered = filter(lambda x: x <= 10, doubled)

result = list(filtered)

print(result)
