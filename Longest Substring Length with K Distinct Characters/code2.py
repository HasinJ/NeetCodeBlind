def characterReplacement(s, k):
    hash = dict()
    left=0
    result = 0
    highest = -1
    for right in range(len(s)):
        hash[s[right]] = hash.get(s[right],0) + 1
        highest = max(highest, hash[s[right]])
        while (right-left+1)-hash[highest] > k:
            hash[s[left]] -= 1
            left+=1
        result = max(right-left+1,result)
    return result





print(characterReplacement("AABABBA",1))
