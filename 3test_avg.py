first_test_m1 = int (input("Enter the marks in the first test: "))
second_test_m2 = int (input("Enter the marks in second test: "))
third_test_m3 = int (input("Enter the marks in third test: "))

if (first_test_m1 > second_test_m2):
    if (second_test_m2 > third_test_m3):
        total = first_test_m1 + second_test_m2
    else: 
        total = first_test_m1 + third_test_m3
elif (first_test_m1 > third_test_m3):
    total = first_test_m1 + third_test_m2
else:
    total = second_test_m2 + third_test_m3
    
Avg = total / 2
print ("The average of the best two test marks is: ",Avg)
