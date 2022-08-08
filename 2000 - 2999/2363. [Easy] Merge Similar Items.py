# https://leetcode.com/problems/merge-similar-items/

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        seen = defaultdict(lambda: 0)
        
        for (value, weight) in items1: 
            seen[value] += weight
        
        for (value, weight) in items2: 
            seen[value] += weight
            
        ans = [(key, seen[key]) for key in seen]
        ans.sort() 
        
        return ans 
        
        
        
