#number of digits in a given number.
N = int(input("Enter a number: "))
count = 0
while N > 0:
    N //= 10
    count += 1  
print("Number of digits:", count)   

