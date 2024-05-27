# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        ans = 0 
        
        for key in counter: 
            if counter[key] == 2: 
                ans ^= key 
                
        return ans 
        
