from functools import reduce

numbers = [1, 2, 3, 4]

running_total = reduce(lambda acc, num: acc + [acc[-1] + num], numbers[1:], [numbers[0]])

print(running_total)
