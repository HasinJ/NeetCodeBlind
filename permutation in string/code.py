


def checkInclusion(s1: str, s2: str) -> bool:
    res = False;
    window, need = {}, {}
    length = 0
    left = 0

    for i in s1:
        need[i] = need.get(i,0) + 1

    for i in range(len(s2)):
        c = s2[i]

        print(c,":")
        if c in s1:
            window[c] = window.get(c,0) + 1
            length += 1

            while(window[c] > need[c]):

                window[s2[left]] = window.get(s2[left]) - 1
                if(window[s2[left]] == 0): window.pop(s2[left])
                length-=1
                left+=1

            if length == len(s1): return True
            #print(window)

        else:
            #print("reset")
            window = {}
            checkwindow = 0
            length = 0
            left+=1



    return res

print(checkInclusion("ab","ab")) #true
print(checkInclusion("bcac","acbc")) #true
print(checkInclusion("ab","acb"))
print(checkInclusion("adc","dcda")) #true

print(checkInclusion("ab", "eidboaoo"))
print(checkInclusion("bab", "eidbaaooo"))
print(checkInclusion("ab", "eidbaooo")) #true
print(checkInclusion("hello", "ooolleoooleh"))
print(checkInclusion("abc", "ccbbaa"))
print(checkInclusion("dinitrophenylhydrazine","acetylphenylhydrazine"))


#if ("h" not in "ah"): print("no")
