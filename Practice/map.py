items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = list(map(lambda item: item[1], items))
print(prices)
prices = [item[1] for item in items]
print(prices)

# Get prices greater than or equal to $10
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
filtered = [item for item in items if item[1] >= 10]
print(filtered)