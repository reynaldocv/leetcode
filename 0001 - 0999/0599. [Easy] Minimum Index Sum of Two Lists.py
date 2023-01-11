# https://leetcode.com/problems/minimum-index-sum-of-two-lists/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = defaultdict(lambda: [])
        
        minValue = inf
        
        seen = {}
        
        for (i, word) in enumerate(list1): 
            seen[word] = i 
            
        for (i, word) in enumerate(list2): 
            if word in seen: 
                minValue = min(minValue, seen[word] + i)
                ans[seen[word] + i].append(word)
                
        return ans[minValue]
