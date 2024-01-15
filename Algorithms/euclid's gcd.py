def gcd(a,b):
    if a<b:
        a,b = b,a
    while a%b!=0:
        a,b = b,a%b
    return b

a1 =int(input("enter:"))
b1= int(input("enter:"))
print(gcd(a1,b1))
