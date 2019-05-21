#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        #sorted by end point
        points = sorted(points,key = lambda x: x[1])
        LastHit = - float('inf')
        ret = 0

        for item in points:
            if item[0]>LastHit:
                ret +=1
                LastHit = item[1]
        return ret

