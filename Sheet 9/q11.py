def f1():
    name = "Suyash"
    def f2():
        nonlocal name
        name = "Chaudhary"
    f2()
    print(name)

f1()
