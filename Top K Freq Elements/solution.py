def topKFrequent(nums, k: int):
    res = []
    hash = {}
    freq = [[] for i in range(len(nums) + 1)]
    for i in range(len(nums)):
        hash[nums[i]] = hash.get(nums[i],0) + 1

    for n, c in hash.items():
        freq[c].append(n) #storing based on count
    #print(freq)

    for n in reversed(freq):
        for num in n:
            res.append(num)
            if len(res) == k: return res


    return res

print(topKFrequent([15,15,15,27,27,31],2))
print(topKFrequent([1,2],2))
