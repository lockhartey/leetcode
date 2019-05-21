#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        cur = head
        dic = {}

        while cur:
            dic[cur] = Node(cur.val,None,None)
            cur = cur.next
        cur = head

        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]


