# https://leetcode.com/problems/random-pick-with-blacklist/

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.k = n - len(blacklist)
        self.blacklist = blacklist
        self.blacklist.sort()

    def pick(self) -> int:
        def helper(val):
            idx = bisect_left(self.blacklist, val)
            if idx == len(self.blacklist) or self.blacklist[idx] != val: 
                idx -= 1
                
            return val - idx
        
        random = randint(1, self.k)
        
        start = -1
        end = self.n - 1
        
        while end - start > 1:
            m = (end + start) // 2            
            if helper(m) < random: 
                start = m
            else: 
                end = m
                
        return end
    
# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
