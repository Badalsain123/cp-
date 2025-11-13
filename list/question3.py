n = [1,2,3,4,5]
max=0;
min=0;
for i in range(1,len(n)):
    if(n[i]<n[min]):
        min=i
    if(n[i]>n[max]):
        max=i
print(n[max])
print(n[min])