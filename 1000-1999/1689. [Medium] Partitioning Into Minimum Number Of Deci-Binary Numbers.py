# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        m = len(n)    
        for i in range(m):
            ans = max(ans, int(n[i]))
        return ans
        
