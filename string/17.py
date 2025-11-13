A =  input()
A = A+A
A = ' '.join(ch for ch in A if not
ch.isupper())
for v in 'aeiou':
    A = A.replace(v, '#')
print(A)