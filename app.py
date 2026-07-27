def greet(name):
    return f"Hello, {name}! Welcome to the Git learning lab."


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


if __name__ == "__main__":
    print(greet("Manthan"))
    print(f"Addition result: {add(2, 3)}")
    print(f"Subtraction result: {subtract(10, 4)}")
    print(f"Multiplication result: {multiply(4, 5)}")