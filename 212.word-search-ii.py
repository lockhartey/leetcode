#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
import collections 
class TrieNode(object):
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        cur = self.root
        for char in word:
            cur = cur.child[char]
        cur.end = True

    def search(self,word):
        cur = self.root
        for char in word:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        return cur.end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            ret = []
            trie = Trie()

            for word in words:
                trie.insert(word)
            
            cur = trie.root

            for i in range(len(board)):
                for j in range(len(board[0])):
                    self.dfs(board,cur,i,j,"",ret)
            return ret

    def dfs(self,board,cur,i,j,path,ret):
        if cur.end:
            ret.append(path)
            cur.end = False
        if i< 0 or i>= len(board) or j<0 or j >= len(board[0]):
            return 
        
        tmp = board[i][j]
        if tmp not in cur.child:
            return 
        cur = cur.child[tmp]

        board[i][j] = "*"

        self.dfs(board,cur,i+1,j,path+tmp,ret)
        self.dfs(board,cur,i-1,j,path+tmp,ret)
        self.dfs(board,cur,i,j+1,path+tmp,ret)
        self.dfs(board,cur,i,j-1,path+tmp,ret)
        board[i][j] = tmp

        