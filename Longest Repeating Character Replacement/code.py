def characterReplacement(s: str, k: int) -> int:
    length = 0
    left = 0
    hash = {}
    currChar = s[0]
    for right in range(len(s)):
        if (s[right] in hash):
            hash[s[right]]+=1

        else:
            hash[s[right]]=1
        length = max(length, right-left+1)
    return length


#print(characterReplacement("ABAB",2))
print(characterReplacement("AABABBA",2))
