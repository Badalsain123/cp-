n = int(input(""))
arr = list(map(int,input().split()))
p = 0
f = 0
for i in range(len(arr)):
    if(arr[i]>=35):
        p+=1
    else:
        f+=1
print(p,f)