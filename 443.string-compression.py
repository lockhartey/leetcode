#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
class Solution:
    def compress(self, chars: List[str]) -> int:
        walk,run = 0,0
        while run<len(chars):
            chars[walk] = chars[run]
            count = 1
            while run < len(chars)-1 and chars[run] == chars[run+1]:
                run +=1
                count +=1

            if count >1:
                for c in str(count):
                    chars[walk+1] = c
                    walk+=1

            walk +=1
            run +=1
        return walk



