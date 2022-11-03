
"""
t = 'b' s = 'a'
t = 'a' s = 'a'
t = 'aa' s = 'a'

"""
def minWindow(s: str, t: str) -> str:
    shortest = ""

    if s == t:
        return s
    if len(t) > len(s): return shortest


    left = 0
    hash = {}

    for right in range(len(s)):
        print(right)
        if (s[right] in t): # only do special things when a character in t has been found while moving right pointer
            if (s[right] in hash): hash[s[right]]+=1 #adding to hash
            else: hash[s[right]]=1 #adding to hash



            while len(hash) == len(t): #when all the letters in t has been found


                if (s[left] in t):
                    hash[s[left]]-=1 #only decrement a character from hash if it exists in t
                    if (hash[s[left]] == 0): #if the count for the letter has reached 0, record the length
                        if (len(s[left:right+1]) < len(shortest) or shortest==''): shortest = s[left:right+1]
                        #print(s[left:right+1])
                        hash.pop(s[left])

                left += 1 #move the left pointer



    return shortest

#print(minWindow("ADOBECODEBANC","ABC"))
#print(minWindow("a","a"))
#print(minWindow("a","aa"))
print(minWindow("abc","cba"))
#print(minWindow("a","b"))
#print("abc" == "bca")
