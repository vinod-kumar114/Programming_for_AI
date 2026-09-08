"""You are given a list where each element represents the price of a stock on a particular day. You may choose one day to buy the stock and a later day to sell it. Your task is to determine the maximum possible profit. If no profit can be made, return 0. 
6. Create a function named max_profit(prices).  
7. The buying day must occur before the selling day.  
8. Return the maximum possible profit. """

def max_profit(prices):
    max_p = 0
    copy = sorted(prices.copy())
    min_value = copy.pop()

    for price in prices:
        if price<min_value:
            min_value=price
        elif price-min_value>max_p:
            max_p=price-min_value
    return max_p

p = [1,2,3,9,4,4,8]
# print(max_profit(p))
prices = [100, 180, 260, 310, 40, 535, 695]
print(max_profit(prices))
        
