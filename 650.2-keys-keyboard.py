#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#
class Solution:
    def minSteps(self, n: int) -> int:
        if n== 1:
            return 0

        for i in range(2,n):
            if n%i ==0:
                return(i+self.minSteps(n//i))
        return n



