#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon[0])

        dp = [2**31]*(n-1) + [1]

        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                dp[j] = max(1,min(dp[j:j+2])-row[j])
        return dp[0]



