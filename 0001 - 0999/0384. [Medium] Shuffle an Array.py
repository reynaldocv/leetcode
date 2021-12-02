# https://leetcode.com/problems/shuffle-an-array/384. Shuffle an Array

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.copy = nums.copy()
        

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.copy = self.original.copy()
        return self.original
        
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.copy)
        for i in range(n):
            rdm = random.randint(0, n - 1)
            self.copy[i], self.copy[rdm] = self.copy[rdm], self.copy[i]
        
        return self.copy
            
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
            
