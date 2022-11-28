def productExceptSelf(nums):
    res = []
    print(nums)

    prefix=[]
    for i in range(len(nums)):
        if i==0:
            prefix.append(nums[i])
            continue
        newnum = nums[i]*prefix[i-1]
        prefix.append(newnum)

    postfix=[]
    for i in range(len(nums)):
        postfix.append(0)
    for i in reversed(range(len(nums))):
        if i==len(nums)-1:
            postfix[i] = nums[i]
            continue
        newnum = nums[i]*postfix[i+1]
        postfix[i] = newnum

    for i in range(len(nums)):
        if i == 0:
            res.append(postfix[i])
            continue
        if i == len(nums)-1:
            res.append(prefix[i-1])
            continue
        
    print(prefix)
    print(postfix)

    #for i in range(len(nums)):




    return res

print(productExceptSelf([1,2,3,4]))
