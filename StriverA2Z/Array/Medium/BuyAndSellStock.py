def buy_and_sell_stock(nums:list) ->int:
    minValue = nums[0]
    maxProfit = 0
    for num in nums:
        minValue = min(minValue,num)
        maxProfit = max(maxProfit,num - minValue)
    return maxProfit

prices = [7, 1, 5, 3, 6, 4]
                    
print(buy_and_sell_stock(prices))

