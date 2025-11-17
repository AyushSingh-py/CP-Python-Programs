#filter odd numbers from an old og array
arr=list(map(int,input("Enter Elements: ").split(" ")))
new_arr=[]

for i in arr:
    if(i%2!=0):
        new_arr.append(i)
print("New Array: ",new_arr)