#given an array and increment number generate a new array which contains all values of origianl array increased by increment value
arr=list(map(int,input("Enter Elements: ").split(" ")))
inc=int(input("Enter Increment: "))
new_arr=[]
for i in arr:
    new_arr.append(i+inc)
print("New Array: ",new_arr)