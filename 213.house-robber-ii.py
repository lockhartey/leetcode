#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]

        def dfs(nums):
            prev = now = 0
            for n in nums:
                now,prev = max(now,prev+n),now
            return now
        return max(dfs(nums[1:]),dfs(nums[:-1]))

