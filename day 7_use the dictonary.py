port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
port2={}
for i in range(0,len(port1)):
    index=list(port1)[i]
    value=port1[index]
    port2[value]=index
print(port2)




