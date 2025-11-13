N= int(input())
arr =  list(map(int,input().split()))
for i in range(N):
    sum  = 0
    for j in range(i,N):
        sum += arr[j]
        print(sum)