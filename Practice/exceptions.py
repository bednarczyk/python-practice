from timeit import timeit

code1 = """

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass

"""

print(timeit(code1, number=10000))

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("Your age is", age)

# Raise / throw exceptions


