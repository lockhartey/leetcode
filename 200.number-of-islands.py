#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0]) if m else 0

        def sink(i,j):
            if 0<=i<m and 0<=j<n and grid[i][j] =="1":
                grid[i][j] = "0"
                map(sink,(i+1,i-1,i,i),(j,j,j+1,j-1))
                return 1
            return 0
        return sum(sink(i,j) for i in range(m) for j in range(n))


