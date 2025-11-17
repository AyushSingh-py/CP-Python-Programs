def do_calc(a, b, sign):
    if sign == '+':
        return a + b
    if sign == '-':
        return a - b
    if sign == '*':
        return a * b
    if sign == '/':
        return a / b

x = int(input())
y = int(input())
op = input()
print(do_calc(x, y, op))
