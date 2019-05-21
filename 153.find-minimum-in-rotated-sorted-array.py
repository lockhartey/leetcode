#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1

        while l<r:
            mid = (r+l)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        return nums[l]


