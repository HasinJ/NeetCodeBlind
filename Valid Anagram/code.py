def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    skeys, tkeys = {}, {}
    for i in s:
        skeys[i] = skeys.get(i,0) + 1
    for i in t:
        tkeys[i] = tkeys.get(i,0) + 1
    for key,value in tkeys.items():
        if skeys.get(key,-1) != value: return False
    return True



print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
