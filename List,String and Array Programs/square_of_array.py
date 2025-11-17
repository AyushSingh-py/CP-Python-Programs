#genertae an array include square of og array elements
arr=list(map(int,input("Enter Elements: ").split(" ")))
new_arr=[]
for i in arr:
    new_arr.append(i*i)
print("New Array: ",new_arr)