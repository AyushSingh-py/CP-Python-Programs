def total_marks(nums):
    s = 0
    for n in nums:
        s += n
    return s

lst = list(map(int, input().split()))
print(total_marks(lst))
