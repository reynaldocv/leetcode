# https://leetcode.com/problems/queries-on-a-permutation-with-key/

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i for i in range(1, m + 1)]
        ans = []
        for q in queries: 
            idx = arr.index(q)
            ans.append(idx)
            arr.pop(idx)
            arr.insert(0, q)
        
        return ans
            
            
            
        
