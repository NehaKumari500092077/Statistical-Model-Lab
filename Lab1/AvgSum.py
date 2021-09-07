def avgOfFirstN(n) :
    return (float)(1 + n) / 2;
def sumOfFirstN(n) :
    return (float)(n*(n+1)) / 2;
n = int(input("Enter any natural No. "));
if(n <= 0):
    print("Invalid Input");
else:
    print(avgOfFirstN(n));
    print(sumOfFirstN(n));
