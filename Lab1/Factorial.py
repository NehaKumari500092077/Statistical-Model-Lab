def factorial(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return  n * factorial(n - 1)
    
num = int(input("Enter a no: "));
if(num < 0):
    print("Invalid Input");
else:
    print("Factorial of",num,"is",factorial(num))
