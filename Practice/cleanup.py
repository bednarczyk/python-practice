try:
    file = open("app.py")
finally:
    file.close()

try:
    with open("app.py") as file, open("another.py") as another:
        print("File opened")
except BaseException:
    print("Woops, we couldn't find that file")