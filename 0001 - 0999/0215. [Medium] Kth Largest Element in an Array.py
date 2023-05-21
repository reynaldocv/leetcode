# https://leetcode.com/problems/kth-largest-element-in-an-array/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        return nums[-k]
        
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        
        maxElem = -inf 
        for num in nums:
            maxElem = max(maxElem, num)
            
            counter[num] += 1 
            
        prev = 0 
            
        for num in range(maxElem, -10**4 - 1, -1):
            if num in counter: 
                prev += counter[num]
                
            if prev >= k: 
                return num 
            
        
