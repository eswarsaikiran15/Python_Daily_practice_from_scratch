a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

def gcd(a,b):
    while b!=0:
        a,b=b,a%b  #a%b=remainder when a is divided by b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)  #integer division (//) in LCM

print("gcd of ",a,"and",b,"is",gcd(a,b))
print("lcm of ",a,"and",b,"is",lcm(a,b))

'''
output:
Enter second number: 18
gcd of  48 and 18 is 6
lcm of  48 and 18 is 144
'''