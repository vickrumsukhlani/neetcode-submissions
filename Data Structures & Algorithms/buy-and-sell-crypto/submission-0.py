class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the brute force approach, we be to double loop through
        # the first loop would be the day we buy
        # the inner loop, the day we sell, we calculate the max profit on each day,
        # we would re calculate the value in the innter loop each time, and then at the end if the value is neg
        # return 0
        
        current_profit = 0
        max_profit = 0
        left = 0
        for right in range(len(prices)):
            if prices[left] < prices[right]:
                # we have potential profit
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right
        
        return max_profit


