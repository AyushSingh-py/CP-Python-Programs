def sumd(n):
    return 0 if n == 0 else n % 10 + sumd(n // 10)
n = int(input("Enter number: "))
print(sumd(n))
