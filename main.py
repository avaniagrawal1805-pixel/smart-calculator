
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot perform modulus by zero!"
    return a % b

def calculator():
    while True:
        print("\n===== SMART CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "6":
            print("Thank you for using Smart Calculator!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice! Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

        elif choice == "5":
            print("Result:", modulus(num1, num2))

        elif choice == "6":
            print("Thank you for using Smart Calculator!")
            break
calculator()
