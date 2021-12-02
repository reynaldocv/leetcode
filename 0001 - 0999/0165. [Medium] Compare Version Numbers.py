# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arrVersion1 = version1.split(".")
        arrVersion2 = version2.split(".")
        n = len(arrVersion1)
        m = len(arrVersion2)
        
        for i in range(max(n, m)):
            num1 = int(arrVersion1[i]) if i < n else 0 
            num2 = int(arrVersion2[i]) if i < m else 0 
            if num1 < num2: 
                return -1
            elif num1 > num2: 
                return 1
        
        return 0
            
        
        

