#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        num = []
        for i in s:
            num.append(ord(i) - ord("A")+1)
        ret = 0
        for i in range(len(num)):
            ret += (26**(len(num)-i-1))*num[i]
        print(num)
        return ret

