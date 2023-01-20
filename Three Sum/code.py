

def threeSum(nums):
    res = []
    left, right = 0, len(nums)-1
    nums.sort()

    for curr in range(len(nums)-2):
        left = curr+1
        target = 0 - nums[curr]
        while left<right:
            sum = nums[left] + nums[right]
            if sum == target:
                if [nums[left], nums[right], nums[curr]] not in res:
                    res.append([nums[left], nums[right], nums[curr]])
                    break
            elif sum < target:
                left+=1
            elif sum > target:
                right-=1


    return res

print(threeSum([0,0,0,0]))
