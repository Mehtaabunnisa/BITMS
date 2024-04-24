list1=[2,4,1,-3,-5,7]
sum_P=0
sum_n=0
sum_o=0

for i in list1:
    if i<=0:
        sum_n+=i
    elif i%2==0:
        sum_P+=i
    else:
        sum_o+=i
    
        
print(sum_P)
print(sum_n)
print(sum_o)


    