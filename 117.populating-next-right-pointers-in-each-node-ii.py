#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
        if not root:
            return None
        
        lev = [root]

        while lev:
            new_lev = []
            prev = None
            for node in lev:
                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    new_lev.append(node.left)
                if node.right:
                    new_lev.append(node.right)
            lev = new_lev
        return root
