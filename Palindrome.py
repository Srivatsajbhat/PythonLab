n = int(input("Enter number:"))
num = n
num1 = str(n)
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
    while (num >0):
        digit = num % 10
        print("The number ",digit," is occurred in a given number",num1.count(str(digit)))
        num = num // 10
else:
    print("The number isn't a palindrome!")
