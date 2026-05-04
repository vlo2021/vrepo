def twoSum(nums, target):
    d = {}

    for (index,number) in enumerate(nums):
        d[number] = index
    print(d)

    i = 0
    while i < (len(nums) -1):

        if nums[i] in d and d.get(nums[i]) == i:
            del(d[nums[i]])

        diff = target - nums[i]
        if diff in d:
            return [i,d[diff]]
            break
        i=i+1


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))
