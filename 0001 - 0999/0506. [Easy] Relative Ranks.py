# https://leetcode.com/problems/relative-ranks/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:        
        n = len(score) 
        
        labels = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        
        arr = [i for i in range(n)]
            
        arr.sort(key = lambda item: -score[item])
        
        ans = ["" for i in range(n)]
        
        for (i, ith) in enumerate(arr):
            if i < 3: 
                ans[ith] = labels[i]
                 
            else: 
                 ans[ith] = str(i + 1)
                 
        return ans 
                
        
