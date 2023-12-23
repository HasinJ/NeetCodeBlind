

import collections
def groupAnagrams(strs):
    res = collections.defaultdict(list)

    for word in strs:
        letters = []
        for i in range(0,25): letters.insert(i,0)
        #count = [0] * 26

        for letter in word:
            letters[ord(letter) - ord("a")] += 1
        print(letters)
        res[tuple(letters)].append(word)
    return res.values()




strs = ["eat","tea","tan","ate","nat","bat"]
print(strs)

print(groupAnagrams(strs))
