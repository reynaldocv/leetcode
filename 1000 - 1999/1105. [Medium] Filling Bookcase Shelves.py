# https://leetcode.com/problems/filling-bookcase-shelves/

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @cache
        def helper(idx):
            if idx == n: 
                return 0 
            
            else: 
                ans = inf 
                
                witdh = 0
                height = 0
                
                for i in range(idx, n):
                    witdh += books[i][0]                    
                    height = max(height, books[i][1])
                    
                    if witdh <= shelfWidth:                     
                        ans = min(ans, height + helper(i + 1))
                        
                return ans
        
        n = len(books)
        
        return helper(0)
        
            
