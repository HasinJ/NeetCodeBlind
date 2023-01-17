
def maxProfit(prices):
    profit, right, lowest = 0, 0, prices[0]
    highest = lowest
    for right in range(len(prices)):
        if prices[right] < lowest:
            lowest = prices[right]
            highest = prices[right]
        if prices[right] > highest:
            highest = prices[right]
        profit = max(highest-lowest, profit)
    return profit


print(maxProfit([7,1,5,3,6,4]))
