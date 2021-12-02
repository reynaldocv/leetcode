# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        div = set([])
        for i in range(1, int(n**0.5) + 2, 1):
            if n % i == 0: 
                div.add(i)
                div.add(n//i)
        div.add(n)        
        div = sorted(list(div))
        
        return div[k - 1] if k <= len(div) else -1
        
        
          
