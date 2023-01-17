
"""
t = 'b' s = 'a'
t = 'a' s = 'a'
t = 'aa' s = 'a'

when a letter has been found
ADOBEC

"""
def minWindow(s: str, t: str) -> str:
    shortest = ""

    if s == t:
        return s
    if len(t) > len(s): return shortest


    left = 0
    hash = {}

    for right in range(len(s)):
        if (s[right] in t or s[right] in hash): # only do special things when a character in t has been found while moving right pointer

            if (s[right] in hash): hash[s[right]]+=1 #adding to hash
            else: hash[s[right]]=1 #adding to hash
            t=t.replace(s[right],'',1) #removing it from needing to find


            while len(t)==0: #when all the letters in t has been found
                if (len(s[left:right+1]) < len(shortest) or shortest==''): shortest = s[left:right+1] #record length when there is nothing to be found in t
                if (s[left] in hash):
                    hash[s[left]]-=1 #only decrement a character from hash if it exists in t
                    if (hash[s[left]] == 0): #if the count for the letter has reached 0, remove from hash and insert back into t
                        hash.pop(s[left])
                        t+=s[left]

                left += 1 #move the left pointer
    return shortest

print(minWindow("ADOBECODEBANC","ABC"))
#print(minWindow("a","a"))
#print(minWindow("a","aa"))
#print(minWindow("abc","cba"))
<<<<<<< HEAD
print(minWindow("bbaa","aba"))
print(minWindow("acbbaca","aba"))
=======
print(minWindow("acbacca","aba"))
>>>>>>> ce065ac1e9848372e6460fd01a4ddeee036b25ff
#print(minWindow("a","b"))
#print("abc" == "bca")
