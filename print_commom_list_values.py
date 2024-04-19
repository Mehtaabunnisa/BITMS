mehtaab=[]
n=int(input("enter the list size of mehtaab"))
for i in range(0,n):
    ele=int(input("enter elements"))
    mehtaab.append(ele)
            
saniya=[]
n=int(input("enter the list size of saniya"))
for i in range(0,n):
    ele=int(input("enter elements"))
    saniya.append(ele)

for i in mehtaab:
    for j in saniya:
        if i==j:
            print(i)
            
                        
            
            
            
            
      
