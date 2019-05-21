#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums,reverse =True)[k-1]
        
        
        # mini-heap method
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap,num)
        # for _ in range(len(nums)-k):
        #     heapq.heappop(heap)
        # return heapq.heappop(heap)
