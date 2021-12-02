# https://leetcode.com/problems/random-pick-with-weight/

class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        
        self.probability = []
        prev = 0
        for num in w:             
            self.probability.append((num + prev)/total)
            prev += num
            
    def pickIndex(self) -> int:
        rand = uniform(0, 1)
        idx = bisect_left(self.probability, rand)
        
        return idx
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

