# https://leetcode.com/problems/merge-similar-items/

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        counter = defaultdict(lambda: 0)
        
        for (value, weight) in items1: 
            counter[value] += weight
            
        for (value, weight) in items2: 
            counter[value] += weight
        
        ans = [(key, counter[key]) for key in counter]
        
        ans.sort()
        
        return ans 
        
        
        
