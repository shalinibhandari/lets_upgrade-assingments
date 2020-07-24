str1="what we think we become.we are python programmer"
p=str1.rfind("we")
index=0
while(index<p):
    s=str1.find("we",index,p)
    if(s==-1):
        break
    index=s+2
    print("index Of we",s)
print("insex of we",p)
