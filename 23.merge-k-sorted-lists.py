#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = cur = ListNode(0)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            cur.next = node[2]
            cur = cur.next
            if cur.next:
                heapq.heappush(heap,(cur.next.val,idx,cur.next))
        return dummy.next
            