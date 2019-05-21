#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        cap = [chr(x) for x in range(ord("A"),ord("Z")+1)]
        ret = []

        while n>0:
            ret.append(cap[(n-1)%26])
            n = (n-1)//26
        ret.reverse()
        return "".join(ret)
