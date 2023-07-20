def F(N):
    if N <= 0:
        print("Error: Number of terms must be a positive integer.")
        return
    elif N == 1:
        return [0]
    elif N == 2:
        return [0, 1]
    else:
        f_n = [0, 1]  # fn = [fn-1,fn-2]

        while len(f_n) < N:
            f_n_next = f_n[-1] + f_n[-2]  #Next term fn = fn-1+fn-2
            f_n.append(f_n_next)  #Creating a list of terms
        return f_n


# Accept input from the user
n = int(input("Enter a positive integer (N > 0): "))

# Call the Fibonacci function and display the result or error message
result = F(n)
if result is not None:
    print(f"The numbers till N are: {result}")
