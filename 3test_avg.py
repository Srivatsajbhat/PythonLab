def is_numeric(input_str):
    return input_str.replace(".", "", 1).isdigit()


def calculate_average(test1, test2, test3):
    # Find the minimum mark and exclude it from the calculation
    min_mark = min(test1, test2, test3)
    
    # Calculate the average of the best two marks
    best_average = (test1 + test2 + test3 - min_mark) / 2
    
    return best_average


def get_test_marks():
    while True:
        test1 = input("Enter the first test mark: ")
        test2 = input("Enter the second test mark: ")
        test3 = input("Enter the third test mark: ")
        
        if is_numeric(test1) and is_numeric(test2) and is_numeric(test3):
            return float(test1), float(test2), float(test3)
        else:
            print("Invalid input. Please enter valid numeric test marks.")


def main():
    test1, test2, test3 = get_test_marks()
    best_average = calculate_average(test1, test2, test3)
    print(f"The best average of the two tests is: {best_average:.2f}")


if __name__ == "__main__":
    main()
