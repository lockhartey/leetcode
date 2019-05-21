#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        for i in sorted(intervals,key = lambda x:x[0]):
            if ret and i[0]<=ret[-1][1]:
                ret[-1][1] = max(ret[-1][-1],i[1])
            else:
                ret.append(i)
        return ret

