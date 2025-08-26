n = int(input("Enter a number: "))
for i in range(n):
    for j in range (n - i):
        print("*", end=" ")
    for k in range(2*i):
        print(" ", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()