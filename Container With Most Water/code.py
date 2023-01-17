

def maxArea(height):
    result = 0
    left, right = 0, len(height)-1

    while left < right:
        area = (min(height[left], height[right])) * (right-left) # l*w
        if height[left] < height[right]:
            left+=1
        else:
            right-=1
        result = max(result, area)


    return result


print(maxArea([1,8,6,2,5,4,8,3,7]))
