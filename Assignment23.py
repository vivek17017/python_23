
"""
#Q1

n=int(input("Enter a number"))
if n>=0:
    fac=1
    for e in range(1,n+1):
        fac=fac*e
    print("factorial of",n,"is",fac)
else:
    print("number is invalid")


#Q1
import math
n=int(input("Enter a number "))
f=math.factorial(n)
print("Factorial is",f)

#Q2
n=int(input("Enter a number"))
b=n
a=0
while b:
    a+=1
    b=b//10
print("total number of digits in",n,"is",a)
n=int(input("Enter a number "))
if n<0:
    n=-n
print("Total no of digits is",len(str(n)))

#Q3
n=int(input("Enter a number"))
sum=0
a=0
g=n
while n:
    a=n%10
    sum=sum+a
    n=n//10
print("sum of digits of",g,"is",sum)


n=int(input("Enter a number"))
if n<0:
    n=-n
print("sum of digits is",sum([int(digit) for digit in str(n)]))



#Q4
n=int(input("Enter a number "))
b=''
while n:
    b=str(n%2)+b
    n=n//2
print(b)


"""
#Q5


n=int(input("Enter a number "))
b=''
while n:
    b=str(n%8)+b
    n=n//8
print(b)



