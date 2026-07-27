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
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"4 × 5 = {multiply(4, 5)}")