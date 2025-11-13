N = int(input())
arr = list(map(int,input().split()))
total =  0
for i in range(N):
    total +=arr[i] * (i+1) * (N -i)
print(total)