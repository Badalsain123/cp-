#sum of digits of a number
n=int(input("Enter a number: "))
sum_of_digits = 0
while n > 0:    
    digit = n % 10
    sumofdigits += digit
    n //= 10
print("Sum of digits:", sumofdigits)
