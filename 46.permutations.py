#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        ret = [[]]

        for n in nums:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l,-1,-1):
                    new_ret.append(seq[:i]+[n]+seq[i:])
            ret = new_ret
        return ret

        