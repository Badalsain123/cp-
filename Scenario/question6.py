n  = int(input())
arr = list(map(int,input().split()))
maximum = 0
count = 0
for i in range(len(arr)):
    if(arr[i]==0):
        count+=1
        maximum = max(maximum,count)
    else:
        count = 0
print(maximum)