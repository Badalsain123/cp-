def ps(A,S,E):
    for i in range(S, E+1):
        print(A[i], end=" ")
    print()
def Allsub(A):
    N = len(A)
    for i in range(N):
        for j in range(i, N):
            ps(A,i,j)
A=(1,2,3) 
Allsub(A)           