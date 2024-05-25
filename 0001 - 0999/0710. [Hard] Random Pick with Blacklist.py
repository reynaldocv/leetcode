# https://leetcode.com/problems/random-pick-with-blacklist/

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.arr = sorted(blacklist)
        
        self.n = n        
        self.elems = n - len(blacklist)

    def pick(self) -> int:
        def helper(value):
            idx = bisect_left(self.arr, value)
            
            ans = value - idx + 1
            
            if idx < len(self.arr) and self.arr[idx] == value:
                ans -= 1 
                
            return ans 
        
        ith = randint(1, self.elems)
        
        start = -1 
        end = self.n 
        
        while end - start > 1: 
            mid = (end + start)//2 
            
            if helper(mid) < ith:
                start = mid 
                
            else: 
                end = mid 
                
        return end                 

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
