# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0 
        
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else: 
                j += 1
            
        return ans
        
class Solution2:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        coordX1, coordX2 = {}, {}
        for (start, end) in firstList: 
            coordX1[start] = 1
            coordX1[end] = -1
        for (start, end) in secondList: 
            coordX2[start] = 1
            coordX2[end] = -1
            
        idx1 = [*coordX1]
        idx2 = [*coordX2]
        
        prev = 0
        start = None
        ans = []
        i, j = 0, 0
        while i < len(idx1) and j < len(idx2):
            x1, x2 = idx1[i], idx2[j]
            x, _, first = min((x1, -coordX1[x1], True), (x2, -coordX2[x2], False))
            prev += coordX1[x1] if first else coordX2[x2]
            if prev == 2: 
                start = x
            elif prev == 1 and start != None:
                ans.append([start, x])
            elif prev == 0: 
                start = None
            if first: 
                i += 1
            else: 
                j += 1
        
        return ans
                
