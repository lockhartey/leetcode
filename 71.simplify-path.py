#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i in ("","."):
                pass
            elif i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+"/".join(stack)

