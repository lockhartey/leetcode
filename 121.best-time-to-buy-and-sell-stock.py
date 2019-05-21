#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        min_price = float('inf')

        for p in prices:
            min_price = min(p,min_price)
            profit = p - min_price
            ret = max(profit,ret)
        return ret

