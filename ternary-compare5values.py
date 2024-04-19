a=int(input("enter the a:"))
b=int(input("enter the b:"))
c=int(input("enter the c:"))
d=int(input("enter the d:"))
e=int(input("enter the e:"))

print("a is greater" if a>b and a>c and a>d and a>e else "b is greater" if b>a and b>c and b>d and b>e else "c is grestest" if c>a and c>b and c>d and c>e else "d is greater" if d>a and d>b and d>c and d>e else "e is greater")