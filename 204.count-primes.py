#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        res = [True]*n
        res[0] = res[1] = False
        for i in range(2,n):
            if res[i]:
                for j in range(2,(n-1)//i+1):
                    res[i*j] = False
        return sum(res)


