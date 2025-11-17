# Q - Print Numbers N to 1 using recursion.

n = int(input("Enter a number: "))
def Num(x):
    if x == 0:
        return
    print(x, end=' ')
    Num(x - 1)

Num(n)
