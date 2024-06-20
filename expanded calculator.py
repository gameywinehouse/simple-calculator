import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def exponent(x, y):
    return x ** y

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error! Invalid input for logarithm."

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error! Cannot take square root of a negative number."

def inverse_square_root(x):
    if x > 0:
        return 1 / math.sqrt(x)
    else:
        return "Error! Invalid input for inverse square root."

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def trunc(x):
    return math.trunc(x)

def mod(x, y):
    if y != 0:
        return x % y
    else:
        return "Error! Division by zero in modulus."

def print_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Logarithm")
    print("7. Square Root")
    print("8. Inverse Square Root")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Truncate")
    print("13. Modulus")
    print("14. Exit")

def get_operation_choice():
    return input("Enter choice (1-14): ")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        print_menu()
        choice = get_operation_choice()
        
        if choice == '14':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '13']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
            elif choice == '5':
                print(f"{num1} ** {num2} = {exponent(num1, num2)}")
            elif choice == '6':
                base = get_number("Enter base for logarithm: ")
                result = logarithm(num1, base)
                if result == "Error! Invalid input for logarithm.":
                    print(result)
                else:
                    print(f"log base {base} of {num1} = {result}")
            elif choice == '13':
                result = mod(num1, num2)
                if result == "Error! Division by zero in modulus.":
                    print(result)
                else:
                    print(f"{num1} % {num2} = {result}")
        elif choice in ['7', '8', '9', '10', '11', '12']:
            num = get_number("Enter number: ")
            if choice == '7':
                result = square_root(num)
                if result == "Error! Cannot take square root of a negative number.":
                    print(result)
                else:
                    print(f"Square root of {num} = {result}")
            elif choice == '8':
                result = inverse_square_root(num)
                if result == "Error! Invalid input for inverse square root.":
                    print(result)
                else:
                    print(f"Inverse square root of {num} = {result}")
            elif choice == '9':
                print(f"sin({num}) = {sin(num)}")
            elif choice == '10':
                print(f"cos({num}) = {cos(num)}")
            elif choice == '11':
                print(f"tan({num}) = {tan(num)}")
            elif choice == '12':
                print(f"trunc({num}) = {trunc(num)}")
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()