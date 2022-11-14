

import collections
def groupAnagrams(strs):
    print(strs)
    res = collections.defaultdict(dict)
    hash = collections.defaultdict(dict)
    for x in range(len(strs)):
        for y in range(len(strs[x])):
            c = strs[x][y]
            hash[c] = hash.get(c,0) + 1
        print(hash)
        res[hash][[].append(strs[x])]


    return res

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
