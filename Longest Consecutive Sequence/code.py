

def longestConsecutive(nums):
    finalres = 0
    count = {}
    visited = {}


    for i in range(len(nums)): #building count
        count[nums[i]] = count.get(nums[i],0) + 1
        visited[nums[i]] = False

    for visitingnum, hasvisited in visited.items():
        if(hasvisited) == True: continue
        res=0
        while visitingnum in visited:
            print(f"visiting: {visitingnum}")
            res = count[visitingnum] + res
            visited[visitingnum] = True
            visitingnum = visitingnum - 1
            print(visited)
        print("res:", res)
        """

        if (visitingnum + 1) in visited:
            res = count[visitingnum] + res
            visited[visitingnum] = True
            visitingnum = visitingnum + 1
        """



    return finalres


print("ans hehe: ",longestConsecutive([100,4,1,5,3,2]))
#print(longestConsecutive([100,4,200,1,3,2]))
#print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
