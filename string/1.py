n  = int(input())
s = input()
s  = input()
vowels = 0
const = 0
for i in range(n):
    for ch in s:
        if ch.lower() in "aeiou":
            vowels +=1
        elif ch.isalpha():
            const +=1
    print(vowels, const)