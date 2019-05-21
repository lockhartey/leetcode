#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
from heapq import heappush,heappop
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ret = [[-1,0]]

        def addsky(pos,height):
            if height!=ret[-1][1]:
                ret.append([pos,height])

        position = set([b[0] for b in buildings]+[b[1] for b in buildings])

        #live buildings
        live = []

        i = 0

        for t in sorted(position):
            #add the buildings whose left side is lefter than position t
            while i<len(buildings) and buildings[i][0]<=t:
                heappush(live,(-buildings[i][2],buildings[i][1]))
                i+=1
            #remove the building in heap whose right side is lefter than t
            while live and live[0][1]<=t:
                heappop(live)

            #pick the highest exsiting buildings at this moments
            h = -live[0][0] if live else 0

            addsky(t,h)
        return ret[1:]
        


