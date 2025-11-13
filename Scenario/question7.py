n = int(input())
arr = list(map(int,input().split()))
highest = arr[0]
count = 0
for i in range(1,len(arr)):
    if(arr[i]>highest):
        highest = arr[i]
        count+=1
print(count)