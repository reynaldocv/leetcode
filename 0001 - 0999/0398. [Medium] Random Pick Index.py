# https://leetcode.com/problems/random-pick-index/

class Solution:

    def __init__(self, nums: List[int]):
        self.indexs = defaultdict(lambda: [])
        
        for (i, num) in enumerate(nums):
            self.indexs[num].append(i)
        
    def pick(self, target: int) -> int:
        return choice(self.indexs[target])
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
