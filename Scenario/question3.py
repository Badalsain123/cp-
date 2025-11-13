n = int(input())
arr = list(map(int,input().split()))
h = arr[0]
l = arr[0]
for i in range(1, len(arr)):
    if(h<arr[i]):
        h = arr[i]
    if(l>arr[i]):
        l = arr[i]
print(h,l)