list1=[1,2,3,4,5]
list2=["a","b","c","d","e"]
dict1={}
for i in range(0,len(list1)):
    dict1[list1[i]]=(list2[i])
    
print(dict1,type(dict1))
