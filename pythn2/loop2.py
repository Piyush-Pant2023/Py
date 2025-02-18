num=8
prime=True
for i in range(2,num):
    if(num%i==0):
        prime=False
        break
if(prime==True):
    print("no is prime")
else:
    print("no is composite")