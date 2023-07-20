def is_even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    try:
        num = int(input("Enter a number: "))
        result = is_even_or_odd(num)
        print(f"The number {num} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
