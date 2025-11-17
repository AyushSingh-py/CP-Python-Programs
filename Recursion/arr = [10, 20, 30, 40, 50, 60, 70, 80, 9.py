arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # sorted list
x = int(input("Enter number to search: "))
low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        print("Found at index:", mid)
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not Found")
