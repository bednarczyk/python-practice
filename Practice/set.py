numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# Union
print(first | second)

# Intersection
print(first & second)

# Difference
print(first - second)

# Symmetric difference (in either fist or second, but not both)
print(first ^ second)

