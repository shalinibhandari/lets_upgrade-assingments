A = [6, 0, 8, 2, 3, 0, 4, 0, 1]
a2=[]
A.sort()
for i in range(0,len(A)):
    if(A[i]!=0):
        a2.append(A[i])
       

index=len(a2)
for i in range(0,len(A)):
    if(A[i]==0):
        a2.append(A[i])
print(a2)
