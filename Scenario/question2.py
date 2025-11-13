n = int(input())
arr = list(map(int,input().split()))
c = []
for i in range(len(arr)):
    if(arr[i]%2==0):
        c.append(arr[i])
print(c)        