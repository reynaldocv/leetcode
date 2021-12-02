# https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        n = len(difficulty)
        m = len(worker)
        
        arr = [(difficulty[i], profit[i]) for i in range(n)]
        arr.sort()
        
        diff = [a for (a, _) in arr]
        prof = [b for (_, b) in arr]
        
        for i in range(1, n):
            prof[i] = max(prof[i], prof[i - 1])
        
        ans = 0
        for w in worker:
            idx1 = bisect_right(diff, w)
            if idx1 != 0: 
                ans += prof[idx1 - 1]
                
        return ans
                
        
