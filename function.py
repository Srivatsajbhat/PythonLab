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
        return None  # Division by zero is not defined

def modulo(x, y):
    if y != 0:
        return x % y
    else:
        return None  # Modulo operation with zero is not defined

def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print(f"Addition: {add(num1, num2)}")
        print(f"Subtraction: {subtract(num1, num2)}")
        print(f"Multiplication: {multiply(num1, num2)}")
        
        result_div = divide(num1, num2)
        if result_div is not None:
            print(f"Division: {result_div}")
        else:
            print("Division by zero is not allowed.")
        
        result_mod = modulo(num1, num2)
        if result_mod is not None:
            print(f"Modulo: {result_mod}")
        else:
            print("Modulo operation with zero is not allowed.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")


if __name__ == "__main__":
    main()
