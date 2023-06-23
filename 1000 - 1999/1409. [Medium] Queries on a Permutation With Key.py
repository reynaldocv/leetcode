# https://leetcode.com/problems/queries-on-a-permutation-with-key/

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i + 1 for i in range(m)]
        
        ans = []
        
        for num in queries: 
            idx = arr.index(num)
            
            ans.append(idx)
            
            arr.pop(idx)            
            arr.insert(0, num)
            
        return ans 
        
            
            
        
