def ok(x):
    return x%2==0

seq = [1,2,3,4,5,6,7,8]
f = list(filter(ok, seq))
print(f)
