# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter = defaultdict(lambda: 0)
        
        ans = []
        
        for num in nums: 
            counter[num] += 1 
            
            if counter[num] > 1:
                ans.append(num)
                
        return ans 
            
