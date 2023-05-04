https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1 for _ in range(rowIndex + 1)]
        
        num = rowIndex 
        den = 1 
        
        for i in range(1, rowIndex + 1):
            ans[i] = ans[i - 1]*num//den
            
            num -= 1 
            den += 1 
            
        return ans 
    
      
