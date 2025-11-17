#given an array of n integer where all numbers occurs in even numbers of time except one which occurs odd numbers of time.find that number.
#first line of the input conatins an integer n,denoting the size of array.
#next line of the input contains n space separated integers denoting the elements of the array.
n=int(input("Enter the size of the array: "))
arr=list(map(int,input("Enter the elements of the array: ").strip().split()))[:n]
result=0
for num in arr:
    result=result^num
print("The number which occurs odd number of times is:",result)


