


def minWindow(s: str, t: str) -> str:
    length = len(s)
    result = [0,0]
    left = 0
    need = {}
    have = {}
    accumulatedHave = 0
    accumulatedNeed = 0

    #filling in the other hashmap with the count
    for i in t:
        #adding to need
        if (i in need): need[i]+=1
        else:
            #adding unique character to need
            need[i]=1
            accumulatedNeed+=1
    print(accumulatedNeed)


    for right in range(len(s)):
        if(s[right] in need):
            #update count
            if ((s[right] in have)): have[s[right]]+=1 #adding to have
            else: have[s[right]]=1 #adding to have

        #comparing what we just added to what we need
        if (s[right] in need):
            if(have[s[right]] == need[s[right]]): #if what we're adding's count is equivalent to what's in our need
                accumulatedHave+=1
            #if we then have what we need, shrink left and update haves if necessary
            while(accumulatedHave == accumulatedNeed):
                if(right-left+1 < length):
                    length = right-left+1
                    result = [left, right]
                    print(left, right)

                if(s[left] in have):
                    have[s[left]]-=1
                    if(have[s[left]] != need[s[left]]): accumulatedHave-=1
                left+=1
            #print(s[result[0]:result[1]+1])


    return s[result[0]:result[1]+1]




print(minWindow("ADOBEC","ABC"))
#print(minWindow("a","a"))
#print(minWindow("a","aa"))
#print(minWindow("abc","cba"))
#print(minWindow("acbacca","aba"))
#print(minWindow("a","b"))
#print("abc" == "bca")
