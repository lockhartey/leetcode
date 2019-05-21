#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # v1,v2 = (map(int,v.split('.')) for v in (version1,version2))
        # d = len(v2) - len(v1)
        # return cmp(v1+[0]*d,v2+[0]*-d)

        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))

        d = len(v2)-len(v1)
        if d>0:
            v1 = v1 +[0]*d
        elif d<0:
            v2 = v2 + [0]*-d

        for i in range(len(v1)):
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
        return 0
