#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        if not root:
            return 0
        def dfs(node):
            l = r = 0
            ls = rs = float('-inf')

            if node.left:
                l,ls = dfs(node.left)
                l = max(l,0)
            if node.right:
                r,rs = dfs(node.right)
                r = max(r,0)
            return node.val+max(l,r), max(node.val+l+r,rs,ls)
        
        return dfs(root)[1]


