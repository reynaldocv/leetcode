# https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        def helper(k):
            for (i, cnt) in enumerate(count): 
                if k <= cnt:
                    return i
                else: 
                    k -= cnt
            return -1
        
        
        minElem = 256
        maxElem = -1
        moda = (0, -1)
        n = 0 
        aSum = 0 
        for (i, cnt) in enumerate(count):
            if cnt != 0: 
                n += cnt
                aSum += cnt*i
                minElem = min(minElem, i)
                maxElem = max(maxElem, i)
                moda = max(moda, (cnt, i))
                
        if n % 2 == 0: 
            median = (helper(n//2) + helper(n//2 + 1))/2
        else: 
            median = helper(n//2 + 1)
            
        return [minElem, maxElem, aSum/n, median, moda[1]]
                
        
