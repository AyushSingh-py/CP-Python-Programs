import math

def check_square(num):
    root = int(math.sqrt(num))
    if root * root == num:
        return root
    return -1

n = int(input())
print(check_square(n))
