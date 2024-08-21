# https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        starts = []
        indexs = []        
        
        for (ith, (start, _)) in enumerate(intervals):
            idx = bisect_left(starts, start)
            
            starts.insert(idx, start)
            indexs.insert(idx, ith)
            
        ans = []
        
        for (start, end) in intervals: 
            idx = bisect_left(starts, end)
            
            if idx == n: 
                ans.append(-1)
                
            else: 
                ans.append(indexs[idx])
            
        return ans
        
