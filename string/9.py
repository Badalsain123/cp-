A = input().split()
res = [word[::-1] for word in A]
print(' '.join(res))