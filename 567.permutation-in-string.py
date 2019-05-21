#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        map1 = [0]*26
        map2 = [0]*26

        i=0
        while i<len(s1):
            map1[ord(s1[i])-ord('a')] +=1
            map2[ord(s2[i])-ord('a')] +=1
            i+=1

        if map1 == map2:
            return True

        l=0
        r = i
        while r <len(s2):
            map2[ord(s2[r])-ord('a')] +=1
            map2[ord(s2[l])-ord('a')] -=1
            if map1 == map2:
                return True
            
            l+=1
            r +=1
        return False

        

        

