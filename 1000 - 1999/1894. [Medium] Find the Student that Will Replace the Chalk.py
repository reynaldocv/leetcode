# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        
        aSum = [chalk[0]]
        
        for i in range(1, n):
            aSum.append(aSum[-1] + chalk[i])
            
        k = k % aSum[-1]
        
        idx = bisect_left(aSum, k)
        
        if aSum[idx] == k: 
            idx += 1 
            
        return idx
                 
        
        
