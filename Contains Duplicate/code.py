def containsDuplicate(nums):
    distinct = set(nums)
    if len(nums) == len(distinct): return False
    return True

print(containsDuplicate([1,2,3,1]))
