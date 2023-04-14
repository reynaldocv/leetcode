# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        prev = 0 
        
        ans = []
        
        for num in target: 
            diff = num - prev
            
            for _ in range(diff - 1):
                ans.append("Push")
                ans.append("Pop")
                
            ans.append("Push")
            
            prev = num
            
        return ans 
                
