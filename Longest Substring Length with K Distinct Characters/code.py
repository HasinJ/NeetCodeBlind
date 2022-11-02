
def cleandict(d):
    return {k: v for k, v in d.items() if v}

# - Am I shrinking?
# - Am I recording
#   - before decreasing window (before failure)

# - sizes can be found mathematically a good chunk of the time, try not to keep them
#   - sizes and sums are different though
# - recording at the end or the beginning

def longestsubstringkdistinct(arr, k):
    longestSize = 0;
    runningSize = 0;
    left = 0
    hash = {}

    for right in range(len(arr)):

        longestSize = max(longestSize, runningSize) #recording longest window size
        print(longestSize)

        if(hash.get(arr[right]) != None): #update only if it exists
            hash[arr[right]]+=1 #updating the counter in hash
        else:
            hash[arr[right]] = 1
        runningSize+=1 #increasing window size

        while( (len(hash)) >= 3): #removing elements from hash
            print(hash)
            hash[arr[left]] -= 1 #decreasing the counter of wherever the left pointer is
            if hash[arr[left]] == 0: #decreasing the dict size
                hash.pop(arr[left])
            left+=1 #moving left pointer to the right
            runningSize-=1 #decreasing window size

            if left==right: break


    return longestSize



arr = ["A","A","A","H","H","I","B","C"]
print(longestsubstringkdistinct(arr, 3))
#print(len({}))

#test = {"A": 0, "B":2}
#print(test)
#test = cleandict(test)
#print(test)
