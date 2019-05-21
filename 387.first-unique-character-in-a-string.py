#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        for c,count in d.items():
            if count==1:
                return s.index(c)
        return -1



