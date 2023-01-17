

def isPalindrome(s):
    str1, str2, strInput = "", "", ""

    for i in s.upper():
        i = f"{i.strip()}"
        print(f"{i}{i.isalpha()}")
        if i.isalpha(): strInput += i

    p1, p2 = 0, len(strInput)-1
    if len(strInput)==1: return False
    while p1 < p2:
        str1+=strInput[p1]
        str2+=strInput[p2]
        p1+=1
        p2-=1
    print(f"str1:{str1} str2:{str2}")
    if str1 == str2: return True
    return False




#print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("p0"))
