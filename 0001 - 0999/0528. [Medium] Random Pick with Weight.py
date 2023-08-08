# https://leetcode.com/problems/random-pick-with-weight/

class Solution:

    def __init__(self, w: List[int]):
        aSum = sum(w)
        
        self.probability = [0]
        
        for num in w: 
            self.probability.append(self.probability[-1] + num/aSum)
            
        self.probability.pop(0)        
        
    def pickIndex(self) -> int:
        rand = random.uniform(0, 1)
        
        ans = bisect_left(self.probability, rand) 
        
        return ans 
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

