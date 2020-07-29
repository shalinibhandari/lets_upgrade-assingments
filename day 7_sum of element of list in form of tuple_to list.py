
list1=[(1,2),(3,4),(5,6),(4,5)]
list2=[]
sum1=0
for i in range (0,len(list1)):
    p=list1[i]
    
    for j in range(0,len(p)):
        s=p[j]
        sum1+=s
    list2.append(sum1)
    sum1=0
print(list2)
    

    
