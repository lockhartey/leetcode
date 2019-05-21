#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        prev = 0
        lev = [(root,1)]
        while lev:
            node,level = lev.pop(0)
            if level> prev:
                ret = node.val
                prev = level
            if node.left:
                lev.append((node.left,level+1))
            if node.right:
                lev.append((node.right,level+1))
        return ret



