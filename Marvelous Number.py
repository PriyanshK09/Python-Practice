r1=int(input("starting range "))
r2=int(input("ending range "))

k=int(input("target num "))

count =0
for i in range(r1,r2+1):
    if(i-int(str(i)[::-1]))%k==0:
        count+=1
print(count)