# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m, n = len(firstList), len(secondList)
        
        i, j = 0, 0 
        
        ans = []
        
        while i < m and j < n: 
            (start1, end1) = firstList[i]
            (start2, end2) = secondList[j]
            
            maxStart = max(start1, start2)
            minEnd = min(end1, end2)
            
            if maxStart <= minEnd:
                ans.append((maxStart, minEnd))
                
            if end1 < end2: 
                i += 1 
                
            else: 
                j += 1 
                
        return ans       
