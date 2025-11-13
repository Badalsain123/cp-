N =  int(input())
arr = list(map(int,input().split()))
sum  = arr[0]
total = 0
for i in arr:
    total = max(i, total + i)
    sum = max(sum, total)
print(sum)
    