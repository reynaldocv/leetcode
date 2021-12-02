# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def helper(cur):
            ans = 0 
            next_ = cur + 1
            
            while cur <= n: 
                ans += min(n - cur + 1, next_ - cur)
                cur *= 10
                next_ *= 10
            
            return ans
        
        cur = 1
        
        while k - 1 > 0:            
            nodes = helper(cur)            
            if(k > nodes):
                k -= nodes
                cur += 1
            else:
                cur *= 10
                k -= 1
        
        return cur
