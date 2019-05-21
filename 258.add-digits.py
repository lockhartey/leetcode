#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
class Solution:
    def addDigits(self, num: int) -> int:
        if num ==0:
            return num
        else:
            return num%9 or 9

