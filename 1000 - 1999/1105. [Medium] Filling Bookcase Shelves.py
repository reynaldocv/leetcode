# https://leetcode.com/problems/filling-bookcase-shelves/

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:        
        @cache
        def helper(idx):
            if idx == n:
                return 0 
            else: 
                w = h = 0 
                ans = inf
                for j in range(idx, n):
                    w += books[j][0]
                    if w > shelfWidth: 
                        return ans
                    h = max(h, books[j][1])
                    ans = min(ans, h + helper(j + 1))
                    
                return ans
            
        n = len(books)
        
        return helper(0)
            
