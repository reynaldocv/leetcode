# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = {}
        for num in nums: 
            counter[num] = counter.get(num, 0) + 1
            
        keys = [*counter]
        keys.sort(reverse = True)
        
        ans = 0
        
        for i in range(len(keys) - 1): 
            ans += counter[keys[i]]
            counter[keys[i + 1]] += counter[keys[i]] 
    
        return ans
            
        
        
