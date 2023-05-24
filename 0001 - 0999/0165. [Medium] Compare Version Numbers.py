# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        
        m, n = len(version1), len(version2)
        
        for i in range(max(n, m)):
            val1 = int(version1[i]) if i < m else 0
            val2 = int(version2[i]) if i < n else 0
            
            if val1 < val2: 
                return -1
            
            elif val1 > val2: 
                return 1 
            
        return 0 
        
        

