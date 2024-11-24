#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        min_price = float('inf')  # 最小値を追跡
        max_profit = 0  # 最大利益を追跡
        
        for price in prices:
            # その時点までの最小価格を更新
            min_price = min(min_price, price)
            # その価格での利益を計算し、最大利益を更新
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
            
        return max_profit
# @lc code=end

