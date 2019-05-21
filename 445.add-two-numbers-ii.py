#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None

        val1 = 0
        while l1:
            val1 = val1*10 + l1.val
            l1 = l1.next
        
        val2 = 0
        while l2:
            val2 = val2*10 + l2.val
            l2 = l2.next

        ret = val1+val2

        head = ListNode(None)
        cur = head
        for c in str(ret):
            cur.next = ListNode(int(c))
            cur = cur.next
        return head.next

