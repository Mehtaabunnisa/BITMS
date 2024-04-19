name=input("enter name:")
l=len(name)
for i in range(l):
    for j in range(l):
        if i==j or i+j==l-1:
            print(name[j],end='')
        else:
            print(' ',end=' ')
    print()
    
name=input("enter name:")
l=len(name)
for i in range(l):
    for j in range(l):
        if i==j or i+j==l-1:
            print(name[i],end='')
        else:
            print(' ',end=' ')
    print()