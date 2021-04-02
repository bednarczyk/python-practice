class Point:

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __cmp__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(isinstance(point, Point))
point.draw()
print(str(point))
point2 = Point(2, 3)
print(point2 > point)
add_point = point + point2
print(add_point)


class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

#    price = property(get_price, set_price)

product = Product(10)
print(product.price)

# Inheritance

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

class Mammal(Animal):
    def walk(self):
        print("walk")

    def __init__(self):
        super().__init__()
        self.weight = 2

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
f = Fish()
f.eat()
print(m.age)