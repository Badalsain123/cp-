#print all factors / divisor of a given +ve number.

N=int(input("enter number: "))
i =1
while(i<=N):
    if(N % i == 0):
        print(i)
    i += 1