x=[int(x) for x in input().split()]
print(x)
sum_P=0
sum_n=0
sum_o=0

for i in x:
    if i<=0:
        sum_n+=i
    elif i%2==0:
        sum_P+=i
    else:
        sum_o+=i
    
        
print(sum_P)
print(sum_n)
print(sum_o)



