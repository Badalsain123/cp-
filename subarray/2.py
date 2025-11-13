N = int(input())
arr = list(map(int,input().split()))
for i in range(N):
    for j in range(i, N):
        print(*arr[i:j+1])
        