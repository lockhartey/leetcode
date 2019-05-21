#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0]) if m else 0

        ret = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]=="X" and (j<1 or  board[i][j-1]==".") and (i<1 or board[i-1][j]=="."):
                    ret +=1
        return ret


