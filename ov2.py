# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "❌ Cannot divide by zero" if b == 0 else a / b

if __name__ == "__main__":
    print("Simple Calculator 🧮")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    op = input("Choose (+, -, *, /): ")

    if op == "+":
        print("Result:", add(x, y))
    elif op == "-":
        print("Result:", subtract(x, y))
    elif op == "*":
        print("Result:", multiply(x, y))
    elif op == "/":
        print("Result:", divide(x, y))
    else:
        print("Invalid operator")