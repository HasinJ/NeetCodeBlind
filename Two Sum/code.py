def twoSum(nums, target: int):
    hash = {}
    for i in range(len(nums)):
        hash[nums[i]] = i

    for i in range(len(nums)):
        curr = target - nums[i]
        if curr in hash:
            if i!=hash[curr]: return [i,hash[curr]]



print(twoSum([2,7,11,15], 9))
print(twoSum([3,3], 6))
