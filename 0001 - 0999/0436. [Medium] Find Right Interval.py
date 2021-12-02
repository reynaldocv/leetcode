# https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        if n == 1: 
            return [-1]
        
        arr = []
        for (i, (a, b)) in enumerate(intervals):
            insort(arr, (a, i))
            
        ans = []
        for (a, b) in intervals: 
            idx = bisect_left(arr, (b, 0))
            if idx == n: 
                ans.append(-1)
            else: 
                ans.append(arr[idx][1])
            
        return ans
        
        
        
