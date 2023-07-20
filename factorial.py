def factorial(num):
    if num < 0:
        return None  # Factorial is not defined for negative numbers
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result


def main():
    try:
        num = int(input("Enter a number to find its factorial: "))
        result = factorial(num)
        if result is not None:
            print(f"The factorial of {num} is: {result}")
        else:
            print("Factorial is not defined for negative numbers.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
