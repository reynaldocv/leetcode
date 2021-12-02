# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = [0 for i in range(left, right + 1)]
        
        for (start, end) in ranges:
            for idx in range(start, end + 1):
                if left <= idx <= right:
                    ans[idx - left] = 1
        
        return len(ans) == sum(ans)
      
                
        
