#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        lev = [root]

        while lev and lev[0]:
            new_lev = []
            prev = None
            for node in lev:
                if prev:
                    prev.next = node
                prev = node

                new_lev.append(node.left)
                new_lev.append(node.right)
            lev = new_lev
        return root
