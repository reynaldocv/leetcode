# https://leetcode.com/problems/shuffle-an-array/384. Shuffle an Array

class Solution:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        
        self.nums = [num for num in nums]
        
    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        idxs = []
        seen = set()
        
        while len(idxs) < self.n: 
            idx = randint(0, self.n - 1)
            
            while idx in seen: 
                idx = randint(0, self.n - 1)
            
            idxs.append(idx)
            seen.add(idx)

        return [self.nums[idx] for idx in idxs]
            
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
            
  
