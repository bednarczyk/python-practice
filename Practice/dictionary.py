# Like a hashmap <k, v>

point = {"x": 1, "y": 2}
dict = dict(x=1, y=2)
print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for key in point:
    print(key, point[key])
for x in point.items():
    print(x)

# Comprehensions:
values = {x: x * 2 for x in range(5)}
print(values)

