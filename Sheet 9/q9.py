name = "abc"
print(name)

def f1():
    name = "def"
    print(name)

print(name)
f1()

def f2():
    global name
    name = "ghi"
    print(name)

print(name)
f2()
print(name)
