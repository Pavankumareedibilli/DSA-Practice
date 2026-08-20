def max_profit(prices:list)->int:
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] - prices[i-1] > 0:
            profit = profit + prices[i] - prices[i-1]
    return profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))