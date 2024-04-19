try:
    n=int(input("enter num:"))
    assert n%2==0
except:
    print("not even num")
else:
    resiprocal=1/n
    print(resiprocal)