# https://leetcode.com/problems/xor-queries-of-a-subarray/submissions/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        
        for num in arr: 
            prefix.append(prefix[-1] ^ num)
            
        ans = []
            
        for (start, end) in queries: 
            ans.append(prefix[end + 1]^prefix[start])
            
        return ans 
            
        
        
