nums = [1,2,3,4]
pair = []
for i in range(len(nums) - 1):
    if i % 2 == 0:
        for j in range(0, nums[i]):
            pair.append(nums[i + 1])
print(pair)