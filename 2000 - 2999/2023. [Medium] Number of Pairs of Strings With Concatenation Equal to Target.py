# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/ 

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(target)
        
        counter = defaultdict(lambda: 0)
        
        for num in nums: 
            counter[num] += 1 
            
        ans = 0 
            
        for i in range(1, n):
            prefix = target[: i]
            suffix = target[i: ]
            
            if prefix != suffix:             
                ans += counter[prefix]*counter[suffix]
                
            else: 
                ans += (counter[prefix] - 1)*counter[prefix]
            
        return ans 
        
        
            
