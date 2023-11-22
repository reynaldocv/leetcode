# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums) 
        
        elems = defaultdict(lambda: [])
        
        for i in range(n):
            for (j, num) in enumerate(nums[i]):
                elems[i + j].insert(0, num)
                
        m = len(elems)
        
        ans = []
        
        for i in range(m):
            ans.extend(elems[i])
            
        return ans 
                
        
                
            
            
        
        
            
