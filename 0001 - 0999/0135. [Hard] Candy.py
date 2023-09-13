# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]
        
        for i in range(1, n):
            if ratings[i - 1] < ratings[i]:
                left[i] += left[i - 1]
        
        for i in range(n - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                right[i] += right[i + 1]
            
        ans = 0 
        for i in range(n):
            ans += max(left[i], right[i])
            
        return ans
        
        
