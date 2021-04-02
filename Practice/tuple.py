point1 = 1, 2
print(type(point1))
point2 = 1,
print(type(point2))
point3 = point1 + point2
print(type(point3))
group = (1, 2) * 3
print(group)
my_list = [1, 2]
my_tuple = tuple([my_list])
triplet = (1, 2, 3)
x, y, z = triplet
if 2 in triplet:
    print("exists")

