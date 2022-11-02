

def maxProfit(prices) -> int:
    currentSum = 0
    profit = 0
    left = 0
    for right in range(len(prices)):
        profit = max(profit,prices[right]-prices[left])
        if (prices[right] < prices[left]):
            left = right

    return profit



print(maxProfit([7,1,5,3,6,4]))
