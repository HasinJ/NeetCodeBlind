
from collections import deque

def maxSlidingWindow(nums, k: int):
    print("nums:", nums, "k:", k)
    d = deque()

    for i in range(len(nums)):

        if d:
            while nums[i] < d[0]:
                d.popleft()
                print(d, "popping")
        d.append(nums[i])
        k-=1

maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
