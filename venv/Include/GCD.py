def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


a=input("Podaj a: ")
b=input("Podaj b, mniejsze od a: ")
a=int(a)
b=int(b)
print("NWD: ",gcd(a,b))