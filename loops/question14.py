
n = int(input("Enter a number: "))

for i in range(n, 0, -1):  # loop starts from n down to 1
    for j in range(n - i):
        print("_", end="")
    for j in range(i):
        print("*", end="")
    print()
