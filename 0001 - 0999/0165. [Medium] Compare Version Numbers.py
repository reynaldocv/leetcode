# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split(".")
        arr2 = version2.split(".")
        
        m, n = len(arr1), len(arr2)
        
        for i in range(max(m, n)):
            val1 = int(arr1[i]) if i < m else 0 
            val2 = int(arr2[i]) if i < n else 0 
            
            if val1 != val2:
                return -1 if val1 < val2 else 1
            
        return 0 
            
        

