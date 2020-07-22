num=int(input("Enter the number"))
count=0
for i in range(2,num):
    if(num%i==0):
        count=1
if(count==1):
    print("the no is not prime no")
else:
    print("the no is prime number")
