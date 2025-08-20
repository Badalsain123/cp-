num=int(input("Enter the number: "))
sum_odd = 0
for i in range(1, num):
    if i % 2 != 0:
        sum_odd += i       
print("Sum of odd numbers:", sum_odd)