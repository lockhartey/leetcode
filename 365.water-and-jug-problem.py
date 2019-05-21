#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if not z:
            return True
        if y==0 or x+y<z:
            return False
        a,b = x,y
        while y:
            r = x%y
            x = y
            y = r
            # print("x==>%s||y==>%s"%(x,y))
        return not bool(z%x)
        

