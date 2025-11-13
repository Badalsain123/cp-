
def print_numbers_reverse(n):
    if n == 0:
        return
    print(n)
    print_numbers_reverse(n - 1)
print_numbers_reverse(5)