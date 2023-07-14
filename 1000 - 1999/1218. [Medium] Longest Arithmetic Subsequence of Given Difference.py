# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = defaultdict(lambda: 0)
        
        ans = 0 
        
        for num in arr: 
            seen[num] = 1 + seen[num - difference]
            
            ans = max(ans, seen[num])
            
        return ans 
            
        
            
        
