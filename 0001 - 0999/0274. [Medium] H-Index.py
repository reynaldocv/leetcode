# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        ans = -inf
        for (i, val) in enumerate(citations):
            if val != 0: 
                if val >= n - i: 
                    ans = max(ans, n - i)
                else: 
                    ans = max(ans, val)
            else: 
                ans = max(ans, 0)
          
        return ans
        
