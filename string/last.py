n = input()
n = n+n
res = ""
for i in range(0, n):
    if(n[i]>='A' and n[i]<='Z'):
        continue 
    elif n[i] in vowel:
        res=res+'#'
    else:
        res
            