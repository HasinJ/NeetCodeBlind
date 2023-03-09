def containsDuplicate(nums):
    unique = set()
    for i in range(len(nums)):
       if nums[i] not in unique: unique.add(nums[i])
       else: return True
    return False

print(containsDuplicate([1,2,3,1]))
