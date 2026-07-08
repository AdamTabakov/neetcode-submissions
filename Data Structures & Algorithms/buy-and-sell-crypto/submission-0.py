class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1

        best_profit = 0

        while right < len(prices):

            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                best_profit = max(profit, best_profit)
            else:
                left = right
            
            right +=1
        
        return best_profit


        
        