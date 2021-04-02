# Generator objects are iterable
# Unlike lists, values are not stored in memory
# In each iteration they generate a new value

from sys import getsizeof

from Practice.class_practice import Point

from moshpdf.moshpdf import pdf2text


values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))

point = Point(1, 2)

pdf2text()

if __name__ == "__main__":
    print("Now this module can be run like a script")




