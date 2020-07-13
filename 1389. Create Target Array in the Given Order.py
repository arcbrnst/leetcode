nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
lst = []
i = 0
x = 0
while x != len(nums):
    lst.insert(index[i], nums[x])
    i += 1
    x += 1

print(lst)
