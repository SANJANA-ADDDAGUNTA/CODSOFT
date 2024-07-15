def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1 , n2):
    if n2 == 0:
        return "Error: Division by zero!"
    return n1 / n2
def calculator():
    print("Select operation:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")

    choice = input("Enter choice (1 or 2 or 3 or 4 ): ")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{n1} + {n2} = {add(n1, n2)}")
    elif choice == '2':
        print(f"{n1} - {n2} = {subtract(n1, n2)}")
    elif choice == '3':
        print(f"{n1} * {n2} = {multiply(n1, n2)}")
    elif choice == '4':
        print(f"{n1} / {n2} = {divide(n1, n2)}")
    else:
        print("Invalid input, Please enter a valid choice.")

while True:
    calculator()
    again = input("Do you want to continue? (yes/no): ").lower()
    if again != 'yes':
        print("Exit")
        break
