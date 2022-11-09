


def checkInclusion(s1: str, s2: str) -> bool:
    res = False;
    have, need = {}, {}
    acchave , accneed = 0, 0

    for i in s1:
        if (i in need): need[i]+=1
        else:
            need[i]=1
            accneed+=1

    right=0
    while right < len(s2):
        c = s2[right]
        print(c)
        #print(c,need)
        if (c in need): #something is found
            for i in range(right, right+len(s1)):
                if(i>len(s2)): return False
                if(c in need):
                    have[c] = have.get(c,0) + 1
                if(c not in need):
                    have={}
                    acchave+=1
                    break
                if acchave==len(s1): return True
        right+=1



        #if(acchave==accneed): return True

    return res

print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
print(checkInclusion("bab", "eidbaaooo"))

#if ("h" not in "ah"): print("no")
