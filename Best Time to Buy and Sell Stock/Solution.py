class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        profit =  0
        for price in prices:
            current_profit = price - lowest_price
            profit = max(profit,current_profit)
            lowest_price = min(price,lowest_price)
        return profit
        
