

def lengthOfLongestSubstring(s: str) -> int:
    maxlength, string = 0, ""
    left = 0
    count = set()

    for right in range(len(s)):
        c = s[right]

        while c in count:
            count.remove(s[left])
            left+=1

        count.add(c)

        if right-left+1 > maxlength:
            maxlength = right-left+1
            string = s[left:right+1]


    return maxlength




print(lengthOfLongestSubstring("pwwkew"))
