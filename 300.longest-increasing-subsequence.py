#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #we keep a tail array which keep the last element of sequence whose length is tail's index +1
        #example [10,9,2,5,3,4]

        # round1: deal 10
        # tail[0] = 10

        # round2 : deal 9
        #tail[0] = 9 (current number small than the mi numeber, so replace)

        # round3 : deal 2
        #tail[0] = 2

        # round4: deal 5
        #tail[0] =2
        #tail[1] = (2) 5 (because current number larger than the max, so we add current number to the longest sequence to a new one)

        # round5: deal 3
        # tail[0] = 2
        # tail[1] = 3

        #round6: deal 4 
        #tail[0] = 2
        #tail[1] = 3
        #tail[2] = 4
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size




