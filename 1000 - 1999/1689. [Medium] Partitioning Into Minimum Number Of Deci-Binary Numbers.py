# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        ans = "0" 
        
        for char in n: 
            ans = max(ans, char) 
            
        return int(ans)
        
