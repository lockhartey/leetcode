#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        lev = [root]
        ret = []
        direct = True

        while lev:
            new_lev = []
            if direct:
                ret.append([n.val for n in lev])
            else:
                ret.append([n.val for n in lev[::-1]])
        
            for node in lev:
                if node.left:
                    new_lev.append(node.left)
                if node.right:
                    new_lev.append(node.right)
            lev = new_lev
            direct = not direct
        return ret

