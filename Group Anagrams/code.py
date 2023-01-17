

import collections
def groupAnagrams(strs):
    res = collections.defaultdict(dict)
    arr = []
    for x in range(len(strs)):
        for y in range(len(strs[x])):
            c = strs[x][y]
            print(c)


    return res

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
