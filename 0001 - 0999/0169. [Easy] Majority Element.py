# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
                
            if num == candidate: 
                count += 1 
                
            else:
                count -= 1 

        return candidate
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        ans = (0, 0)
        
        for num in nums: 
            counter[num] += 1 
            
            ans = max(ans, (counter[num], num))
            
        return ans[1]
