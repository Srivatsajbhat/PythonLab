def prime_number(a):
   k=0
   for i in range(2,a//2+1):
       if(a%i==0):
           k=k+1
   if(k<=0):
       print("Number is prime")
   else:
       print("Number isn't prime")
       
def count_each_digit(a):
    ans = 0
    while (a >0):
        ans = ans+1
        b = a % 10
        a = a // 10
        print(b)
        
   


a=int(input("Enter number: "))
prime_number(a)
count_each_digit(a)
