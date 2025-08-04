#!/usr/bin/env python3

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def main():
    print("=== Welcome to the CLI Calculator ===")
    print("Available operations: +  -  *  /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == '+':
            result = add(num1, num2)
        elif op == '-':
            result = subtract(num1, num2)
        elif op == '*':
            result = multiply(num1, num2)
        elif op == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
