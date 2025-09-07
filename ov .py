# simple_program.py

def greet(name):
    return f"Hello, {name}! 👋"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))